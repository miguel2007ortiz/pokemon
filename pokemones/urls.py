"""
URL configuration for pokemones project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pokedex import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rutas Pokémon
    path('', views.home, name='home'),
    path('pokemon/nuevo/', views.crear_pokemon, name='crear_pokemon'),
    path('pokemon/<int:pk>/editar/', views.editar_pokemon, name='editar_pokemon'),
    path('pokemon/<int:pk>/eliminar/', views.eliminar_pokemon, name='eliminar_pokemon'),
    
    # Rutas Entrenadores
    path('entrenadores/', views.lista_entrenadores, name='lista_entrenadores'),
    path('entrenadores/nuevo/', views.crear_entrenador, name='crear_entrenador'),
    path('entrenadores/<int:pk>/', views.detalle_entrenador, name='detalle_entrenador'),
    path('entrenadores/<int:pk>/editar/', views.editar_entrenador, name='editar_entrenador'),
    path('entrenadores/<int:pk>/eliminar/', views.eliminar_entrenador, name='eliminar_entrenador'),

    # Rutas Gyms
    path('gimnasios/', views.lista_gyms, name='lista_gyms'),
    path('gimnasios/nuevo/', views.crear_gym, name='crear_gym'),
    path('gimnasios/<int:pk>/editar/', views.editar_gym, name='editar_gym'),
    path('gimnasios/<int:pk>/eliminar/', views.eliminar_gym, name='eliminar_gym'),

    # Rutas Backup (Cajas PC)
    path('backups/', views.lista_backups, name='lista_backups'),
    path('backups/nuevo/', views.crear_backup, name='crear_backup'),
    path('backups/<int:pk>/editar/', views.editar_backup, name='editar_backup'),
    path('backups/<int:pk>/eliminar/', views.eliminar_backup, name='eliminar_backup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)