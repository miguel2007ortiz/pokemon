from django import forms
from .models import Entrenador, Pokemon, Gym, Backup

class EntrenadorForm(forms.ModelForm):
    class Meta:
        model = Entrenador
        fields = [
            'nombre',
            'apellido',
            'documento',
            'medallas',
            'clasifico',
            'pueblo',
            'liga',
            'profesor_asignado',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Ash'}),
            'apellido': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Ketchum'}),
            'documento': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. ENT100'}),
            'medallas': forms.NumberInput(attrs={'class': 'form-input', 'min': 0, 'max': 8}),
            'clasifico': forms.CheckboxInput(attrs={'style': 'width: auto; transform: scale(1.3);'}),
            'pueblo': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Pueblo Paleta'}),
            'liga': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Liga Añil'}),
            'profesor_asignado': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Prof. Oak'}),
        }

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = [
            'nombre',
            'estadistica',
            'tipo_elemento',
            'habilidad',
            'evoluciones',
            'imagen_url',
            'imagen',
            'es_legendario',
            'entrenador',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Pikachu'}),
            'estadistica': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Base stat / HP'}),
            'tipo_elemento': forms.Select(attrs={'class': 'form-input'}),
            'habilidad': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Electricidad estática'}),
            'evoluciones': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Raichu'}),
            'imagen_url': forms.URLInput(attrs={'class': 'form-input', 'placeholder': 'https://... (URL de la imagen)'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-input'}),
            'es_legendario': forms.CheckboxInput(attrs={'style': 'width: auto; transform: scale(1.3);'}),
            'entrenador': forms.Select(attrs={'class': 'form-input'}),
        }

class GymForm(forms.ModelForm):
    class Meta:
        model = Gym
        fields = [
            'ciudad',
            'lider_de_gimnasio',
            'tipo_elemento',
            'medalla',
            'telefono',
            'region',
            'entrenador',
        ]
        widgets = {
            'ciudad': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Ciudad Plateada'}),
            'lider_de_gimnasio': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Brock'}),
            'tipo_elemento': forms.Select(attrs={'class': 'form-input'}),
            'medalla': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Medalla Roca'}),
            'telefono': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. 555-0101'}),
            'region': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Kanto o Johto'}),
            'entrenador': forms.Select(attrs={'class': 'form-input'}),
        }

class BackupForm(forms.ModelForm):
    class Meta:
        model = Backup
        fields = [
            'entrenador',
            'numero_pokemones_guardados',
            'profesor_que_los_cuida',
            'items',
            'region',
        ]
        widgets = {
            'entrenador': forms.Select(attrs={'class': 'form-input'}),
            'numero_pokemones_guardados': forms.NumberInput(attrs={'class': 'form-input', 'min': 0}),
            'profesor_que_los_cuida': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Profesor Oak'}),
            'items': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Poké Balls, Pociones, Piedra Fuego'}),
            'region': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Kanto, Johto'}),
        }