from django.contrib import admin
from django.contrib.admin.decorators import display
from gestionContenidos.models import Peliculas

class PeliculasAdmin(admin.ModelAdmin):
    list_display=('titulo','categoria','imagen','fecha','youtube')
    search_fields=("titulo","descripcion",)
    list_filter=("categoria","fecha")
    date_hierarchy="fecha"

# Register your models here.
admin.site.register(Peliculas,PeliculasAdmin)
