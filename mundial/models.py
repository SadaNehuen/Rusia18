# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Grupo(models.Model):
    letra = models.CharField(max_length=1)

    def __str__(self):
        return "Grupo " + self.letra

class Seleccion(models.Model):
    nombre = models.CharField(max_length=60)
    img_url = models.CharField(max_length=200)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Sede(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Ronda(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Resultado(models.Model):
    goles_local = models.IntegerField(default=None)
    goles_visitante = models.IntegerField(default=None)
    penales_local = models.IntegerField(default=None)
    penales_visitante = models.IntegerField(default=None)
    ganador_id = models.IntegerField(default=None)

class Partido(models.Model):
    fecha = models.DateTimeField()
    sede = models.ForeignKey(Sede, on_delete=None)
    ronda = models.ForeignKey(Ronda, on_delete=None)
    resultado = models.ForeignKey(Resultado, on_delete=None)
    jugado = models.BooleanField(default=False)

class Pronostico(models.Model):
    partido = models.ForeignKey(Partido, on_delete=None)
    resultado = models.ForeignKey(Resultado, on_delete=None)
    puntos = models.IntegerField(default=0)