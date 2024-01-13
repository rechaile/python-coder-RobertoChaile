from django import forms

class formSong(forms.Form):
    name = forms.CharField(max_length=100)
    album = forms.CharField(max_length=100)
    year = forms.IntegerField()
    artist = forms.CharField(max_length=100)
    genre = forms.CharField(max_length=100)
    
class formArtist(forms.Form):
    name = forms.CharField(max_length=100)
    genre = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    
class formAlbum(forms.Form):
    name = forms.CharField(max_length=100)
    artist = forms.CharField(max_length=100)
    genre = forms.CharField(max_length=100)
    year = forms.IntegerField()

class formUser(forms.Form):
    username = forms.EmailField()
    password = forms.CharField(max_length=100)