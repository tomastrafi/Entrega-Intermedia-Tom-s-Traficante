from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre=models.CharField(max_length=40)
    rol=models.CharField(max_length=40)
    trabajo=models.CharField(max_length=40)
    edad=models.IntegerField()

class Zona(models.Model):
    provincia=models.CharField(max_length=40)
    ciudad=models.CharField(max_length=40)
    barrio=models.CharField(max_length=40)
    codigo_postal=models.IntegerField()

class Deporte(models.Model):
    deporte_favorito=models.CharField(max_length=40)
    club=models.CharField(max_length=40)
    posicion=models.CharField(max_length=40)
    años_jugando=models.IntegerField()