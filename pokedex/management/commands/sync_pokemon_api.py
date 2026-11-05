import requests
from django.core.management.base import BaseCommand
from pokedex.models import Pokemon

class Command(BaseCommand):
    help = 'Descarga los Pokémon desde la PokéAPI y los guarda en la base de datos'

    def handle(self, *args, **options):
        # Mapeo completo de tipos inglés -> español
        tipo_map = {
            'grass': 'planta',
            'fire': 'fuego',
            'water': 'agua',
            'electric': 'electrico',
            'poison': 'veneno',
            'bug': 'bicho',
            'normal': 'normal',
            'ground': 'tierra',
            'rock': 'roca',
            'psychic': 'psiquico',
            'flying': 'volador',
            'fairy': 'hada',
            'fighting': 'lucha',
            'ice': 'hielo',
            'ghost': 'fantasma',
            'dragon': 'dragon',
            'steel': 'acero',
            'dark': 'siniestro',
        }

        cantidad = 1025
        url = f'https://pokeapi.co/api/v2/pokemon?limit={cantidad}'
        
        self.stdout.write(f'Conectando con PokéAPI para obtener {cantidad} Pokémon...')
        response = requests.get(url)

        if response.status_code != 200:
            self.stdout.write(self.style.ERROR('Error al conectar con la PokéAPI'))
            return

        data = response.json()
        results = data.get('results', [])

        for index, item in enumerate(results, start=1):
            poke_detail = requests.get(item['url']).json()
            
            nombre = poke_detail['name'].capitalize()
            stats_base = poke_detail['stats'][0]['base_stat']
            imagen_url = poke_detail['sprites']['front_default']
            habilidad = poke_detail['abilities'][0]['ability']['name'] if poke_detail['abilities'] else 'Ninguna'
            
            tipo_api = poke_detail['types'][0]['type']['name']
            tipo_espanol = tipo_map.get(tipo_api, 'otro')

            # Detectar legendarios básicos de la Gen 1
            es_legendario = nombre in ['Articuno', 'Zapdos', 'Moltres', 'Mewtwo', 'Mew']

            Pokemon.objects.update_or_create(
                nombre=nombre,
                defaults={
                    'estadistica': stats_base,
                    'imagen_url': imagen_url,
                    'habilidad': habilidad,
                    'tipo_elemento': tipo_espanol,
                    'es_legendario': es_legendario,
                }
            )
            self.stdout.write(f'[{index}/{cantidad}] Guardado: {nombre}')

        self.stdout.write(self.style.SUCCESS(f'¡Los {cantidad} Pokémon se sincronizaron con éxito en PostgreSQL!'))