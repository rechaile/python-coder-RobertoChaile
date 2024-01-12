from django import forms

class formSong(forms.Form):
    name = forms.CharField(max_length=100)
    album = forms.CharField(max_length=100)
    year = forms.IntegerField()
    artist = forms.CharField(max_length=100)
    genre = forms.CharField(max_length=100)