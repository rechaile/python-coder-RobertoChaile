from django.contrib import admin

# Register your models here.
from musicapp.models import *


admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(User)