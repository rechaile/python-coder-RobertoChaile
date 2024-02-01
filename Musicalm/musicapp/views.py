from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from musicapp.forms import *
from musicapp.models import *
from django.contrib.auth.decorators import login_required
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# Create your views here.

def inicioSesion(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            passw = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password = passw)
            if user:
                login(request, user)
                
                return render(request,"musicapp/inicio.html", {"mensaje": f"Bienvenido {user}"} )
            else:
                return render(request,"musicapp/inicio.html", {"mensaje": f"Los datos ingresados son incorrectos"} )
    else:
        form = AuthenticationForm()

    return render(request,"musicapp/login.html", {"formulario": form})  

def editUser(request):
    usuario_actual = request.user
    
    if request.method == 'POST':
        
        form = EditarUsuario(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data
            
            usuario_actual.first_name = info["first_name"]
            usuario_actual.last_name = info["last_name"]
            usuario_actual.email = info["email"]
            usuario_actual.set_password = info["password1"]
            usuario_actual.save()
            
            return render(request,"musicapp/inicio.html", {"mensaje": f"Usuario editado correctamente"} )
            
    else:
        form = EditarUsuario(initial = {"first_name": usuario_actual.first_name,
                                        "last_name": usuario_actual.last_name,
                                        "email": usuario_actual.email,
                                        })

    return render(request,"musicapp/editarUsuario.html", {"formulario": form})  


def cerrarSesion(request):
    logout(request)
    return render(request,"musicapp/logout.html")

def registro(request):
    
    if request.method == 'POST':
        form = usuarioRegistro(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get("username")
            form.save()
            return render(request,"musicapp/inicio.html", {"mensaje": f"Usuario creado correctamente"} )
            
    else:
        form = usuarioRegistro()

    return render(request,"musicapp/registro.html", {"formulario": form})  

      
def inicio(request):
   return render(request, "musicapp/inicio.html")

@login_required
def songs(request):
    if not request.user.is_staff:
        return redirect('Inicio')
    return render(request, "musicapp/canciones.html")
@login_required
def artists(request):
    if not request.user.is_staff:
        return redirect('Inicio')
    return render(request, "musicapp/artistas.html")

@login_required
def albums(request):
    if not request.user.is_staff:
        return redirect('Inicio')
    return render(request, "musicapp/albums.html")


def createSong(request):
    if request.method == "POST":
        formCanciones = formSong(request.POST)
        
        if formCanciones.is_valid():
            info = formCanciones.cleaned_data
            
            cancion = Song(name=info['name'], album=info['album'], year=info['year'], artist=info['artist'], genre=info['genre'])
            
            cancion.save()
            
            return render(request, "musicapp/canciones.html")
        
    else:
        
        formCanciones = formSong()
        
        return render(request, "musicapp/crearCancion.html", {"formCancion":formCanciones})


@login_required
def resultSongs(request):
    if not request.user.is_staff:
        return redirect('Inicio')
    
    mensaje = None
    
    if request.method == 'GET' and 'cancion' in request.GET:
        song = request.GET['cancion'].strip()  # Elimina espacios en blanco al principio y al final
        
        if song:  # Verifica si el campo de búsqueda no está vacío
            canciones = Song.objects.filter(name__icontains=song)
        
            if not canciones:
                mensaje = "No se encontraron resultados"
        
            return render(request, "musicapp/canciones.html", {"canciones": canciones, 'cancion': song, 'mensaje': mensaje})
        else:
            mensaje = "El campo de búsqueda está vacío"
    
    else:
        mensaje = None  # Si no se envió el formulario de búsqueda, no se define el mensaje
    
    return render(request, "musicapp/canciones.html", {'mensaje': mensaje})

def allSongs(request):
    canciones = Song.objects.all().order_by('name')
    return render(request, "musicapp/canciones.html", {"canciones": canciones})

def editSong(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    
    if request.method == 'POST':
        form = formSong(request.POST)
        if form.is_valid():
            song.name = form.cleaned_data['name']
            song.album = form.cleaned_data['album']
            song.year = form.cleaned_data['year']
            song.artist = form.cleaned_data['artist']
            song.genre = form.cleaned_data['genre']
            song.save()
            return redirect('canciones')  # Redirigir a la página de canciones
    else:
        form = formSong(initial={
            'name': song.name,
            'album': song.album,
            'year': song.year,
            'artist': song.artist,
            'genre': song.genre
        })

    return render(request, 'musicapp/editSong.html', {'form': form})

def deleteSong(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    
    if request.method == 'POST':
        song.delete()
        return redirect('canciones') 
    
    return render(request, 'musicapp/delete_song.html', {'song': song})


def SearchSongbyMood(request):
    if request.method == 'POST':
        form = BusquedaCancionesForm(request.POST)
        if form.is_valid():
            estado_animo = form.cleaned_data['estado_animo']
            banda_favorita = form.cleaned_data['banda_favorita']
            genero_favorito = form.cleaned_data['genero_favorito']

            # Realizar la búsqueda en la API de Spotify
            resultados = search_spotify(estado_animo, banda_favorita, genero_favorito)

            # Ejemplo de cómo guardar la consulta en la base de datos
            if not request.user.is_anonymous and not request.user.is_staff:
                consulta = ConsultaUsuario.objects.create(usuario=request.user, estado_animo=estado_animo, banda_favorita=banda_favorita, genero_favorito=genero_favorito)
                consulta.save()

            # Verificar si se encontraron resultados
            if resultados:
                # Procesar los resultados y devolverlos a la plantilla HTML
                return render(request, 'musicapp/resultados_busqueda.html', {'form': form, 'resultados': resultados})
            else:
                # Si no se encontraron resultados, mostrar un mensaje en la plantilla HTML
                mensaje = "No se encontraron canciones que coincidan con los criterios de búsqueda."
                return render(request, 'musicapp/resultados_busqueda.html', {'mensaje': mensaje})
    else:
        form = BusquedaCancionesForm()

    return render(request, 'musicapp/resultados_busqueda.html', {'form': form})

def search_spotify(estado_animo, banda_favorita, genero_favorito):
    # Configurar las credenciales del cliente de Spotify
    client_credentials_manager = SpotifyClientCredentials(client_id='TU-CLIENT-ID', client_secret='TU-CLIENT-SECRET')
    
    # Crear una instancia del objeto Spotipy
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Realizar la búsqueda de canciones basadas en la banda favorita y el género favorito
    query = f'artist:{banda_favorita} genre:{genero_favorito}'
    results_canciones = sp.search(q=query, limit=5, type='track')
    
    results_listas = sp.category_playlists(category_id='mood', country='US', limit=1, offset=0)

    # Procesar los resultados de las canciones
    canciones = []
    for track in results_canciones['tracks']['items']:
        cancion = {
            'nombre_cancion': track['name'],
            'artista': track['artists'][0]['name'],
            'album': track['album']['name'] if 'album' in track else '',  # Verificar si la clave 'album' está presente
            'iframe_spotify': track['external_urls']['spotify'] if 'external_urls' in track else '',  # Verificar si la clave 'external_urls' está presente
        }
        canciones.append(cancion)

    # Procesar los resultados de las listas de reproducción
    playlists = []
    for playlist in results_listas['playlists']['items']:
        playlists.append(playlist['id'])

    # Obtener las canciones de las primeras 5 listas de reproducción
    for playlist_id in playlists[:5]:
        playlist_tracks = sp.playlist_tracks(playlist_id, fields='items(track(name, artists(name), album(name), external_urls(spotify))), total', limit=5)
        for track in playlist_tracks['items']:
            cancion = {
                'nombre_cancion': track['track']['name'],
                'artista': track['track']['artists'][0]['name'],
                'album': track['track']['album']['name'] if 'album' in track['track'] else '',  # Verificar si la clave 'album' está presente
                'iframe_spotify': track['track']['external_urls']['spotify'] if 'external_urls' in track['track'] else '',  # Verificar si la clave 'external_urls' está presente
            }
            canciones.append(cancion)

    return canciones
        
def crearArtista(request):
    if request.method == "POST":
        formArtista = formArtist(request.POST)
        if formArtista.is_valid():
            info = formArtista.cleaned_data
            artist = Artist(name=info['name'], genre=info['genre'], country=info['country'])
            artist.save()
            return render(request, "musicapp/artistas.html")
        
    else:  # GET request
        formArtista = formArtist()
        return render(request, "musicapp/crearArtista.html", {'formArtist': formArtista})
    return render(request, "musicapp/crearArtista.html")

@login_required
def resultArtists(request):
    if not request.user.is_staff:
        return redirect('Inicio')
    
    mensaje = None
    
    if request.method == 'GET' and 'artista' in request.GET:
        artista = request.GET.get('artista', '').strip()
        
        if artista:
            artistas = Artist.objects.filter(name__icontains=artista)
        
            if not artistas:
                mensaje = "No se encontraron resultados"
        
            return render(request, "musicapp/artistas.html", {"artistas": artistas, 'artista': artista, 'mensaje': mensaje})
        else:
            mensaje = "El campo de búsqueda está vacío"

    else:
        mensaje = None  # Si no se envió el formulario de búsqueda, no se define el mensaje
    
    return render(request, "musicapp/artistas.html", {'mensaje': mensaje})

def allArtists(request):
    artistas = Artist.objects.all().order_by('name')
    return render(request, "musicapp/artistas.html", {"artistas": artistas})

def createAlbum(request):
    if request.method == "POST":
        formDisco = formAlbum(request.POST)
        if formDisco.is_valid():
            info = formDisco.cleaned_data
            album = Album(name=info['name'], artist=info['artist'], genre=info['genre'], year=info['year'])
            album.save()
            return render(request, "musicapp/albums.html")
        
    else:  # GET request
        formDisco = formAlbum()
        return render(request, "musicapp/crearAlbum.html", {'formAlbum': formDisco})
    return render(request, "musicapp/crearAlbum.html")

@login_required
def resultAlbum(request):
    
    if not request.user.is_staff:
        return redirect('Inicio')
    
    mensaje = None
    
    if request.method == 'GET' and 'album' in request.GET:
        album = request.GET.get('album', '').strip()
        
        if album:
            albums = Album.objects.filter(name__icontains=album)
        
            if not albums:
                mensaje = "No se encontraron resultados"
        
            return render(request, "musicapp/albums.html", {"albums": albums, 'album': album, 'mensaje': mensaje})
        else:
            mensaje = "El campo de búsqueda está vacío"

    else:
        mensaje = None  # Si no se envió el formulario de búsqueda, no se define el mensaje
    
    return render(request, "musicapp/albums.html", {'mensaje': mensaje})

def allAlbums(request):
    albums = Album.objects.all().order_by('name')
    return render(request, "musicapp/albums.html", {"albums": albums})


