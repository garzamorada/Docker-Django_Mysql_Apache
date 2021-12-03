from django.db import models

class Peliculas(models.Model):
        id=models.AutoField(primary_key=True)
        fecha = models.DateTimeField(auto_now_add=True)
        titulo=models.CharField(max_length=250)
        imagen=models.CharField(max_length=100)
        url=models.CharField(max_length=250)
        categoria=models.CharField(max_length=100)
        youtube=models.CharField(max_length=100)
        descripcion=models.TextField()