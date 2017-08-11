# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Grupo, Partido, Seleccion, Pronostico, Sede, Ronda, Resultado

# Register your models here.
admin.site.register(Grupo)
admin.site.register(Seleccion)
admin.site.register(Ronda)
admin.site.register(Sede)
admin.site.register(Pronostico)
admin.site.register(Partido)
admin.site.register(Resultado)