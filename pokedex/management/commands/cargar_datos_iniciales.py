# pokedex/management/commands/cargar_datos_iniciales.py
from django.core.management.base import BaseCommand
from pokedex.models import Entrenador, Gym, Backup

class Command(BaseCommand):
    help = 'Carga 15 entrenadores y 16 gimnasios en 2 regiones (Kanto y Johto)'

    def handle(self, *args, **options):
        # 1. Cargar 15 Entrenadores
        entrenadores_data = [
            ("Ash", "Ketchum", "ENT001", 8, True, "Pueblo Paleta", "Liga Añil", "Profesor Oak"),
            ("Misty", "Waterflower", "ENT002", 5, False, "Ciudad Celeste", "Liga Añil", "Profesor Oak"),
            ("Brock", "Harrison", "ENT003", 6, False, "Ciudad Plateada", "Liga Añil", "Profesor Oak"),
            ("Gary", "Oak", "ENT004", 10, True, "Pueblo Paleta", "Liga Añil", "Profesor Oak"),
            ("Red", "Pallet", "ENT005", 8, True, "Pueblo Paleta", "Liga Añil", "Profesor Oak"),
            ("Blue", "Oak", "ENT006", 8, True, "Pueblo Paleta", "Liga Añil", "Profesor Oak"),
            ("Ethan", "Gold", "ENT007", 8, True, "Pueblo Primavera", "Liga Johto", "Profesor Elm"),
            ("Kris", "Crystal", "ENT008", 7, False, "Pueblo Primavera", "Liga Johto", "Profesor Elm"),
            ("Lyra", "Soul", "ENT009", 8, True, "Pueblo Primavera", "Liga Johto", "Profesor Elm"),
            ("Silver", "Kanto", "ENT010", 8, True, "Ciudad Cerezo", "Liga Johto", "Profesor Elm"),
            ("Lance", "Dragon", "ENT011", 8, True, "Pueblo Caoba", "Liga Johto", "Profesor Elm"),
            ("Erika", "Grass", "ENT012", 4, False, "Ciudad Azulona", "Liga Añil", "Profesor Oak"),
            ("Sabrina", "Psychic", "ENT013", 5, False, "Ciudad Azafrán", "Liga Añil", "Profesor Oak"),
            ("Falkner", "Sky", "ENT014", 3, False, "Ciudad Malvalona", "Liga Johto", "Profesor Elm"),
            ("Whitney", "Miltank", "ENT015", 4, False, "Ciudad Trigal", "Liga Johto", "Profesor Elm"),
        ]

        for nom, ape, doc, med, clasif, pueb, lig, prof in entrenadores_data:
            entrenador, _ = Entrenador.objects.update_or_create(
                documento=doc,
                defaults={
                    'nombre': nom,
                    'apellido': ape,
                    'medallas': med,
                    'clasifico': clasif,
                    'pueblo': pueb,
                    'liga': lig,
                    'profesor_asignado': prof,
                }
            )
            # Crear su caja PC de Backup correspondiente
            Backup.objects.get_or_create(
                entrenador=entrenador,
                defaults={
                    'numero_pokemones_guardados': 6,
                    'profesor_que_los_cuida': prof,
                    'items': 'Poké Balls, Pociones',
                    'region': 'Kanto' if 'Añil' in lig else 'Johto',
                }
            )

        self.stdout.write(self.style.SUCCESS('15 Entrenadores y sus Backups registrados.'))

        # 2. Cargar 16 Gimnasios (8 en Kanto y 8 en Johto)
        gimnasios_data = [
            # Región Kanto (8 Gyms)
            ("Brock", "roca", "Medalla Roca", "Ciudad Plateada", "555-0101", "Kanto"),
            ("Misty", "agua", "Medalla Cascada", "Ciudad Celeste", "555-0102", "Kanto"),
            ("Lt. Surge", "electrico", "Medalla Trueno", "Ciudad Carmín", "555-0103", "Kanto"),
            ("Erika", "planta", "Medalla Arcoíris", "Ciudad Azulona", "555-0104", "Kanto"),
            ("Koga", "veneno", "Medalla Alma", "Ciudad Fucsia", "555-0105", "Kanto"),
            ("Sabrina", "psiquico", "Medalla Pantano", "Ciudad Azafrán", "555-0106", "Kanto"),
            ("Blaine", "fuego", "Medalla Volcán", "Isla Canela", "555-0107", "Kanto"),
            ("Giovanni", "tierra", "Medalla Tierra", "Ciudad Verde", "555-0108", "Kanto"),
            # Región Johto (8 Gyms)
            ("Falkner", "volador", "Medalla Céfiro", "Ciudad Malva", "555-0201", "Johto"),
            ("Bugsy", "bicho", "Medalla Colmena", "Pueblo Azalea", "555-0202", "Johto"),
            ("Whitney", "normal", "Medalla Planicie", "Ciudad Trigal", "555-0203", "Johto"),
            ("Morty", "fantasma", "Medalla Niebla", "Ciudad Iris", "555-0204", "Johto"),
            ("Chuck", "lucha", "Medalla Tormenta", "Ciudad Orquídea", "555-0205", "Johto"),
            ("Jasmine", "acero", "Medalla Mineral", "Ciudad Olivo", "555-0206", "Johto"),
            ("Pryce", "hielo", "Medalla Glaciar", "Pueblo Caoba", "555-0207", "Johto"),
            ("Clair", "dragon", "Medalla Dragón", "Ciudad Endrino", "555-0208", "Johto"),
        ]

        primer_entrenador = Entrenador.objects.first()

        for lider, elem, med, ciu, tel, reg in gimnasios_data:
            Gym.objects.update_or_create(
                ciudad=ciu,
                defaults={
                    'lider_de_gimnasio': lider,
                    'tipo_elemento': elem,
                    'medalla': med,
                    'telefono': tel,
                    'region': reg,
                    'entrenador': primer_entrenador,
                }
            )

        self.stdout.write(self.style.SUCCESS('16 Gimnasios registrados (8 Kanto, 8 Johto).'))