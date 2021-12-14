from django.http import HttpRequest
from django.http import JsonResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render
from gestionContenidos.models import Peliculas

def home(request):
    return render(request,'home.html')

def prueba(request):
    return render(request,'prueba.html')

def peliculas(request):
    if request.method == 'GET':
        peliculas = Peliculas.objects.all().values('titulo', 'imagen','url','categoria','youtube') 
        lista_peliculas=muestraImgFull(list(peliculas))
        return JsonResponse(lista_peliculas, safe=False)

def muestraImgFull(lista):
    for i in range(len(lista)):
        partesImg=lista[i]['imagen'].rpartition('.')
        nuevaImg=partesImg[0]+'.full.'+partesImg[2]
        lista[i]['imagen'] = nuevaImg
    return lista

    