# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth



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
    goles_local = models.IntegerField(null=True, default=None)
    goles_visitante = models.IntegerField(null=True, default=None)
    penales_local = models.IntegerField(null=True, default=None)
    penales_visitante = models.IntegerField(null=True, default=None)
    ganador_id = models.IntegerField(null=True, default=None)

class Partido(models.Model):
    fecha = models.DateTimeField()
    sede = models.ForeignKey(Sede, on_delete=None)
    ronda = models.ForeignKey(Ronda, on_delete=None)
    resultado = models.ForeignKey(Resultado, on_delete=None, null=True)
    jugado = models.BooleanField(default=False)
    partido_selecciones = models.ManyToManyField(Seleccion, through='PartidoSeleccion')

class Pronostico(models.Model):
    partido = models.ForeignKey(Partido, on_delete=None)
    resultado = models.ForeignKey(Resultado, on_delete=None, null=True)
    puntos = models.IntegerField(default=0)
    user = models.ForeignKey(User)

class PartidoSeleccion(models.Model):
    ''' 
    Modelo y tabla de relacion entre Partido y Selecciones. Cada registro de la tabla PartidoSeleccion tiene:
        partido_id -> del partido al que está relacionado
        seleccion_id -> de la seleccion al que está relacinado
        local -> un booleano que indica si la seleccion_id referida en el partido_id referido es local o no.
    
    En la tabla habrá dos regisotrs po
    '''
    partido = models.ForeignKey(Partido)
    seleccion = models.ForeignKey(Seleccion)
    local = models.BooleanField(default=False)

