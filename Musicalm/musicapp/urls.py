from django.urls import path
from musicapp.views import *

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('songs/', songs, name='Canciones'),
    path('albums/', albums, name='Albums'),
    path('artists/', artists, name='Artistas'),
    path('users/', users, name='Usuarios'),
    path('register/', createUsers, name='Registro'),
    path('crearCanciones/', crearCanciones, name='CrearCanciones'),
    path('crearAlbums/', createAlbum, name='CrearAlbums'),
    path('crearArtistas/', crearArtista, name='CrearArtistas'),
]