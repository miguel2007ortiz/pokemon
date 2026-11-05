from django.db import models

# Create your models here.
from django.db import models

class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.CharField(max_length=50, unique=True)
    medallas = models.PositiveIntegerField(default=0)
    clasifico = models.BooleanField(default=False)
    pueblo = models.CharField(max_length=100)
    liga = models.CharField(max_length=100)
    profesor_asignado = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Gym(models.Model):
    TIPO_CHOICES = [
        ('fuego', 'Fuego'),
        ('agua', 'Agua'),
        ('planta', 'Planta'),
        ('electrico', 'Eléctrico'),
        ('roca', 'Roca'),
        ('psiquico', 'Psíquico'),
        ('hielo', 'Hielo'),
        ('dragon', 'Dragón'),
        ('otro', 'Otro'),
    ]
    lider_de_gimnasio = models.CharField(max_length=100)
    tipo_elemento = models.CharField(max_length=20, choices=TIPO_CHOICES)
    medalla = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    region = models.CharField(max_length=100)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.SET_NULL, null=True, blank=True, related_name='gimnasios')

    def __str__(self):
        return f"Gimnasio de {self.ciudad} - Líder: {self.lider_de_gimnasio}"


class Pokemon(models.Model):
    TIPO_CHOICES = [
        ('normal', 'Normal'),
        ('fuego', 'Fuego'),
        ('agua', 'Agua'),
        ('planta', 'Planta'),
        ('electrico', 'Eléctrico'),
        ('veneno', 'Veneno'),
        ('volador', 'Volador'),
        ('tierra', 'Tierra'),
        ('roca', 'Roca'),
        ('psiquico', 'Psíquico'),
    ]

    nombre = models.CharField(max_length=100)
    estadistica = models.IntegerField(default=100, help_text="Total base stats o nivel")
    imagen = models.ImageField(upload_to='pokemons/', null=True, blank=True)
    imagen_url = models.URLField(max_length=500, null=True, blank=True, help_text="Para imágenes importadas desde API")
    habilidad = models.CharField(max_length=100)
    tipo_elemento = models.CharField(max_length=50, choices=TIPO_CHOICES)
    evoluciones = models.CharField(max_length=255, blank=True)
    es_legendario = models.BooleanField(default=False)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.SET_NULL, null=True, blank=True, related_name='pokemones')

    def __str__(self):
        return self.nombre


class Backup(models.Model):
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE, related_name='backups')
    numero_pokemones_guardados = models.PositiveIntegerField(default=0)
    profesor_que_los_cuida = models.CharField(max_length=100)
    items = models.CharField(max_length=255, blank=True)
    region = models.CharField(max_length=100)

    def __str__(self):
        return f"Backup de {self.entrenador.nombre} - {self.region}"