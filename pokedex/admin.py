from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Entrenador, Gym, Pokemon, Backup

@admin.register(Entrenador)
class EntrenadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'documento', 'pueblo', 'medallas', 'clasifico')
    search_fields = ('nombre', 'apellido', 'documento')

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_elemento', 'estadistica', 'es_legendario', 'entrenador')
    list_filter = ('tipo_elemento', 'es_legendario')
    search_fields = ('nombre',)

@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ('ciudad', 'lider_de_gimnasio', 'tipo_elemento', 'region')

@admin.register(Backup)
class BackupAdmin(admin.ModelAdmin):
    list_display = ('entrenador', 'numero_pokemones_guardados', 'profesor_que_los_cuida', 'region')