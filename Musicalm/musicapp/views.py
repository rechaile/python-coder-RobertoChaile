from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from musicapp.forms import *
from musicapp.models import *
from django.contrib.auth.decorators import login_required

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
    return render(request, "musicapp/canciones.html")
@login_required
def artists(request):
    return render(request, "musicapp/artistas.html")

@login_required
def albums(request):
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


