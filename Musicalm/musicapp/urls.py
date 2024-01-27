from django.urls import path
from musicapp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('login/', inicioSesion, name='Login'),
    path('register/', registro, name='Registro'),
    path('editProfile/', editUser, name='EditarPerfil'),
    path('logout/', cerrarSesion, name='logout'),
    path('canciones/', songs, name='canciones'),
    path('albums/', albums, name='Albums'),
    path('artistas/', artists, name='Artistas'),
    path('crearCanciones/', createSong, name='CrearCanciones'),
    path('crearAlbums/', createAlbum, name='CrearAlbums'),
    path('crearArtistas/', crearArtista, name='CrearArtistas'),
    path('resultadosCancion/', resultSongs, name='resultadosCanciones'),
    path('resultadosArtista/', resultArtists, name='resultadosArtistas'),
    path('resultadosAlbum/', resultAlbum, name='resultadosAlbums'),
    path('allSongs/', allSongs, name='all_songs'),
    path('allArtists/', allArtists, name='all_artists'),
    path('allAlbums/', allAlbums, name='all_albums'),
    path('canciones/editar/<int:song_id>/', editSong, name='edit_song'),
    path('canciones/eliminar/<int:song_id>/', deleteSong, name='delete_song'),
]