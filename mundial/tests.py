# -*- coding: utf-8 -*-
import datetime

from __future__ import unicode_literals

from django.utils import timezone
from django.test import TestCase
from .models import Seleccion, Partido, Sede, Ronda, Grupo, Resultado, Pronostico, PartidoSeleccion

def crear_datos_mundial():
    rondas = ["Fase de grupos", "Octavos de final", "Cuartos de final"]
    sedes = ["Moscú", "San Petersburgo", "Rostov del Don"]
    grupos = ["A", "B", "C", "D"]
    selecciones = ["Argentina", "Brasil", "Chile", "Ecuador"]

    ret = {}
    ret["rondas"] = []
    ret["sedes"] = []
    ret["grupos"] = []

    for ronda in rondas:
        r = Ronda(nombre=ronda)
        ret["rondas"].append(r)
    
    for sede in sedes:
        s = Sede(nombre=sede)
        ret["sedes"].append(s)

    for grupo in grupos:
        g = Grupo(nombre=grupo)
        ret["grupos"].append(g)

    s1 = Seleccion(nombre=selecciones[0], img_url="/", grupo=ret["grupos"][0])
    s2 = Seleccion(nombre=selecciones[1], img_url="/", grupo=ret["grupos"][0])
    s3 = Seleccion(nombre=selecciones[2], img_url="/", grupo=ret["grupos"][1])
    s4 = Seleccion(nombre=selecciones[3], img_url="/", grupo=ret["grupos"][1])

    ret["selecciones"] = [s1, s2, s3, s4]

    return ret 

# Create your tests here.

class PartidoModelTests(TestCase):

    def test_relacion_muchos_a_muchos_seleccion(self):
        datos = crear_datos_mundial()
        partido_test = Partido(fecha = timezone.now(), sede = datos["sedes"][0], ronda = datos["rondas"][0])
        partSel = PartidoSeleccion(partido=partido_test, seleccion=datos["selecciones"][0], True)
        partSel2 = PartidoSeleccion(partido=partido_test, seleccion=datos["selecciones"][1], False)
        