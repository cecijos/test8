from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from .models import Videojuego
from .models import Sala
from .models import Comentario
from blog import models
from django.contrib.auth.models import User



class VideojuegoAdmin(admin.ModelAdmin):
    search_fields = ['videojuego_id', 'name']

class SalaAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title','author']

class ComentarioAdmin(admin.ModelAdmin):
    search_fields = ["author__title"]


    list_display = ['title', 'author','added_by' ]
    prepopulated_fields = {'title': ('title',)}
    ordering = ('title', 'author','added_by')

admin.site.register(Videojuego,VideojuegoAdmin)
admin.site.register(Sala,SalaAdmin)
admin.site.register(Comentario,ComentarioAdmin)






