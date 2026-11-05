from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Pokemon, Entrenador, Gym, Backup
from .forms import EntrenadorForm, PokemonForm, GymForm, BackupForm

# --- VISTAS DE POKEMON (CRUD) ---

def home(request):
    query = request.GET.get('q', '').strip()
    tipo_filtro = request.GET.get('tipo', '').strip()
    pokemons_queryset = Pokemon.objects.all()
    if query:
        pokemons_queryset = pokemons_queryset.filter(
            Q(nombre__icontains=query) | Q(habilidad__icontains=query)
        )
    if tipo_filtro:
        pokemons_queryset = pokemons_queryset.filter(tipo_elemento=tipo_filtro)
    pokemons_queryset = pokemons_queryset.order_by('id')

    paginator = Paginator(pokemons_queryset, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'pokemons': page_obj,  # Se pasa también como 'pokemons' por compatibilidad
        'total_pokemons': Pokemon.objects.count(),
        'total_entrenadores': Entrenador.objects.count(),
        'total_gyms': Gym.objects.count(),
        'query': query,
        'tipo_filtro': tipo_filtro,
        'tipos_disponibles': Pokemon.TIPO_CHOICES,
    }
    return render(request, 'pokedex/pokemons.html', context)

def crear_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            poke = form.save()
            messages.success(request, f'¡Pokemon {poke.nombre} registrado con exito!')
            return redirect('home')
        
    else:
        form = PokemonForm()
    return render(request, 'pokedex/formulario_pokemon.html', {'form': form, 'titulo': 'Registrar Nuevo Pokémon'})

def editar_pokemon(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            messages.success(request, f'¡Pokemon {pokemon.nombre} actualizado correctamente!')
            return redirect('home')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'pokedex/formulario_pokemon.html', {'form': form, 'titulo': f'Editar Pokémon: {pokemon.nombre}'})

def eliminar_pokemon(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    if request.method == 'POST':
        nombre = pokemon.nombre
        pokemon.delete()
        messages.success(request, f'El Pokemon {nombre} ha sido eliminado.')
        return redirect('home')
    return render(request, 'pokedex/confirmar_eliminar_pokemon.html', {'pokemon': pokemon})


# --- VISTAS DE ENTRENADOR (CRUD) ---

def lista_entrenadores(request):
    entrenadores = Entrenador.objects.all().order_by('nombre')
    return render(request, 'pokedex/entrenadores.html', {'entrenadores': entrenadores})

def lista_entrenadores(request):
    query = request.GET.get('q', '').strip()
    filtro_clasificado = request.GET.get('clasifico', '').strip()

    entrenadores = Entrenador.objects.all()

    if query:
        entrenadores = entrenadores.filter(
            Q(nombre__icontains=query) |
            Q(apellido__icontains=query) |
            Q(documento__icontains=query) |
            Q(pueblo__icontains=query)
        )

    if filtro_clasificado == 'si':
        entrenadores = entrenadores.filter(clasifico=True)
    elif filtro_clasificado == 'no':
        entrenadores = entrenadores.filter(clasifico=False)

    entrenadores = entrenadores.order_by('nombre')

    context = {
        'entrenadores': entrenadores,
        'query': query,
        'filtro_clasificado': filtro_clasificado,
    }
    return render(request, 'pokedex/entrenadores.html', context)

def detalle_entrenador(request, pk):
    entrenador = get_object_or_404(Entrenador, pk=pk)
    return render(request, 'pokedex/detalle_entrenador.html', {'entrenador': entrenador})

def crear_entrenador(request):
    if request.method == 'POST':
        form = EntrenadorForm(request.POST)
        if form.is_valid():
            nuevo_entrenador = form.save()
            messages.success(request, f'¡Entrenador {nuevo_entrenador.nombre} creado con éxito!')
            return redirect('detalle_entrenador', pk=nuevo_entrenador.pk)
    else:
        form = EntrenadorForm()
    return render(request, 'pokedex/formulario_entrenador.html', {'form': form, 'titulo': 'Registrar Nuevo Entrenador'})

def editar_entrenador(request, pk):
    entrenador = get_object_or_404(Entrenador, pk=pk)
    if request.method == 'POST':
        form = EntrenadorForm(request.POST, instance=entrenador)
        if form.is_valid():
            form.save()
            messages.success(request, f'¡Datos de {entrenador.nombre} actualizados con éxito!')
            return redirect('detalle_entrenador', pk=entrenador.pk)
    else:
        form = EntrenadorForm(instance=entrenador)
    return render(request, 'pokedex/formulario_entrenador.html', {'form': form, 'titulo': f'Editar Entrenador: {entrenador.nombre}'})

def eliminar_entrenador(request, pk):
    entrenador = get_object_or_404(Entrenador, pk=pk)
    if request.method == 'POST':
        nombre = entrenador.nombre
        entrenador.delete()
        messages.success(request, f'El entrenador {nombre} fue eliminado.')
        return redirect('lista_entrenadores')
    return render(request, 'pokedex/confirmar_eliminar.html', {'entrenador': entrenador})

# --- CRUD Y VISTAS DE GYM ---

def lista_gyms(request):
    query = request.GET.get('q', '').strip()
    region_filtro = request.GET.get('region', '').strip()

    gyms = Gym.objects.all()

    if query:
        gyms = gyms.filter(
            Q(ciudad__icontains=query) |
            Q(lider_de_gimnasio__icontains=query) |
            Q(medalla__icontains=query)
        )

    if region_filtro:
        gyms = gyms.filter(region__iexact=region_filtro)

    gyms = gyms.order_by('region', 'id')

    context = {
        'gyms': gyms,
        'query': query,
        'region_filtro': region_filtro,
        'regiones': Gym.objects.values_list('region', flat=True).distinct(),
    }
    return render(request, 'pokedex/gyms.html', context)

def crear_gym(request):
    if request.method == 'POST':
        form = GymForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gimnasio registrado con éxito!')
            return redirect('lista_gyms')
    else:
        form = GymForm()
    return render(request, 'pokedex/formulario_gym.html', {'form': form, 'titulo': 'Registrar Nuevo Gimnasio'})

def editar_gym(request, pk):
    gym = get_object_or_404(Gym, pk=pk)
    if request.method == 'POST':
        form = GymForm(request.POST, instance=gym)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gimnasio actualizado con éxito!')
            return redirect('lista_gyms')
    else:
        form = GymForm(instance=gym)
    return render(request, 'pokedex/formulario_gym.html', {'form': form, 'titulo': f'Editar Gimnasio de {gym.ciudad}'})

def eliminar_gym(request, pk):
    gym = get_object_or_404(Gym, pk=pk)
    if request.method == 'POST':
        gym.delete()
        messages.success(request, '¡Gimnasio eliminado con éxito!')
        return redirect('lista_gyms')
    return render(request, 'pokedex/confirmar_eliminar_gym.html', {'gym': gym})

# --- CRUD Y VISTAS DE BACKUP / CAJAS PC ---

def lista_backups(request):
    """Listado general de todas las cajas PC / Backups con buscador"""
    query = request.GET.get('q', '').strip()
    backups = Backup.objects.all().select_related('entrenador')

    if query:
        backups = backups.filter(
            Q(entrenador__nombre__icontains=query) |
            Q(entrenador__apellido__icontains=query) |
            Q(profesor_que_los_cuida__icontains=query) |
            Q(region__icontains=query) |
            Q(items__icontains=query)
        )

    backups = backups.order_by('entrenador__nombre', 'id')

    context = {
        'backups': backups,
        'query': query,
    }
    return render(request, 'pokedex/backups.html', context)

def crear_backup(request):
    if request.method == 'POST':
        form = BackupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Caja / Backup registrada con éxito!')
            return redirect('lista_backups')
    else:
        form = BackupForm()
    return render(request, 'pokedex/formulario_backup.html', {'form': form, 'titulo': 'Registrar Nueva Caja / Backup'})

def editar_backup(request, pk):
    backup = get_object_or_404(Backup, pk=pk)
    if request.method == 'POST':
        form = BackupForm(request.POST, instance=backup)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Caja / Backup actualizada con éxito!')
            return redirect('lista_backups')
    else:
        form = BackupForm(instance=backup)
    return render(request, 'pokedex/formulario_backup.html', {'form': form, 'titulo': f'Editar Caja PC de {backup.entrenador.nombre}'})

def eliminar_backup(request, pk):
    backup = get_object_or_404(Backup, pk=pk)
    if request.method == 'POST':
        backup.delete()
        messages.success(request, '¡Caja / Backup eliminada con éxito!')
        return redirect('lista_backups')
    return render(request, 'pokedex/confirmar_eliminar_backup.html', {'backup': backup})