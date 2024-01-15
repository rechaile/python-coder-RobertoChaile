from django.urls import path
from musicapp.views import *

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('canciones/', songs, name='canciones'),
    path('albums/', albums, name='Albums'),
    path('artistas/', artists, name='Artistas'),
    path('crearCanciones/', createSong, name='CrearCanciones'),
    path('crearAlbums/', createAlbum, name='CrearAlbums'),
    path('crearArtistas/', crearArtista, name='CrearArtistas'),
    path('resultadosCancion/', resultSongs, name='resultadosCanciones'),
    path('resultadosArtista/', resultArtists, name='resultadosArtistas'),
    path('resultadosAlbum/', resultAlbum, name='resultadosAlbums'),
]