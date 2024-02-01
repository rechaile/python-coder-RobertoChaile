from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Song(models.Model):
    
    def __str__(self):
        return f"Nombre: {self.name} --- Artista: {self.artist}"
    
    name = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    year = models.IntegerField()
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    
class Artist(models.Model):
    
    def __str__(self):
        return f"Nombre: {self.name} --- Artista: {self.genre}"
    
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
class Album(models.Model):
    
    def __str__(self):
        return f"Nombre: {self.name} --- Artista: {self.artist}"
    
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()


class ConsultaUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estado_animo = models.CharField(max_length=100)
    banda_favorita = models.CharField(max_length=100)
    genero_favorito = models.CharField(max_length=100)
    fecha_consulta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consulta de {self.usuario.username} ({self.fecha_consulta})"