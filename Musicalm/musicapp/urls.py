from django.urls import path
from musicapp.views import *

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('canciones/', songs, name='canciones'),
    path('albums/', albums, name='Albums'),
    path('artistas/', artists, name='Artistas'),
    path('usuarios/', users, name='Usuarios'),
    path('registro/', createUsers, name='Registro'),
    path('crearCanciones/', createSong, name='CrearCanciones'),
    path('crearAlbums/', createAlbum, name='CrearAlbums'),
    path('crearArtistas/', crearArtista, name='CrearArtistas'),
    path('resultadosCancion/', resultSongs, name='resultadosCanciones')
]