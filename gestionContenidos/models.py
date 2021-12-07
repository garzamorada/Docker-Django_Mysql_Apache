import os
from django.conf import settings
from django.db import models
from stdimage import StdImageField, JPEGField

class Peliculas(models.Model):
        marvel = 'marvel'
        dc = 'dc'
        fox = 'fox'
        wb = 'wb'
        startrek = 'startrek'
        starwars = 'starwars'
        ListaCatrgorias=[
                (marvel, 'Marvel Studios'),
                (dc, 'DC Cinematic Universe'),
                (fox, '20 Century Fox'),
                (wb, 'Warner Movies'),
                (startrek, 'Star Treck Univese'),
                (starwars, 'Star Wars Universe'),
        ]
        id=models.AutoField(primary_key=True)
        fecha = models.DateTimeField(auto_now_add=True)
        titulo=models.CharField(max_length=250)
        url=models.CharField(max_length=250,default='../pages/player.html',blank=True)
        categoria=models.CharField(max_length=100,choices=ListaCatrgorias)
        youtube=models.CharField(max_length=100)
        descripcion=models.TextField(blank=True)
        imagen=StdImageField(upload_to='images/',default=None,variations={'full': (460, 800)}, delete_orphans=True)