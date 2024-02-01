from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
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


class usuarioRegistro(UserCreationForm):

    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
    
    class Meta:
            model = User
            fields = ["username", "email", "first_name", "last_name", "password1", "password2"]
            
            
class EditarUsuario(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
    class Meta:
            model = User
            fields = [ "email", "first_name", "last_name", "password1", "password2"]
            

class BusquedaCancionesForm(forms.Form):
    estado_animo = forms.CharField(max_length=100)
    banda_favorita = forms.CharField(max_length=100)
    genero_favorito = forms.CharField(max_length=100)