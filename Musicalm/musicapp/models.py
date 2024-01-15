from django.db import models

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    year = models.IntegerField()
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    
class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
