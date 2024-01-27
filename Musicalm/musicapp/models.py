from django.db import models

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
