from django.shortcuts import render
from django.http import HttpResponse
from musicapp.forms import *
from musicapp.models import *

# Create your views here.
def inicio(request):
   return render(request, "musicapp/inicio.html")

def songs(request):
    return render(request, "musicapp/canciones.html")

def artists(request):
    return render(request, "musicapp/artistas.html")


def albums(request):
    return render(request, "musicapp/albums.html")

def users(request):
    return render(request, "musicapp/usuarios.html")

def createUsers(request):
    return render(request, "musicapp/registro.html")

def createSongs(request):
    if request.method == "POST":
        formCanciones = formSong(request.POST)
        if formCanciones.is_valid():
            info = formCanciones.cleaned_data
            
            cancion = Song(name=info['name'],album=info['album'],year=info['year'],artist=info['artist'], genre=info['genre'])
            
            cancion.save()
            
            return render(request, "musicapp/crearCancion.html")
        else: 
            formCanciones = formSong()
        return render(request, "musicapp/crearCancion.html", {'formSong':formCanciones})
def createArtist(request):
    return render(request, "musicapp/crearArtista.html")

def createAlbum(request):
    return render(request, "musicapp/crearAlbum.html")