from django.shortcuts import render, redirect
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



def resultSongs(request):
    
    if request.GET['cancion']:
        
        song=request.GET['cancion']
        
        canciones = Song.objects.filter(name__icontains=song)
        
        return render(request, "musicapp/canciones.html", {"canciones": canciones, 'cancion': song})
    
    else:
        
        respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)


        
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

def createAlbum(request):
    return render(request, "musicapp/crearAlbum.html")