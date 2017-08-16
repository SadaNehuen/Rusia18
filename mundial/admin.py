# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Grupo, Partido, Seleccion, Pronostico, Sede, Ronda, Resultado, PartidoSeleccion

# Register your models here.
class PartidoSeleccionInline(admin.StackedInline):
    model = PartidoSeleccion
    extra = 0
    
class PartidoAdmin(admin.ModelAdmin):
    inlines = [PartidoSeleccionInline]

admin.site.register(Partido, PartidoAdmin)
admin.site.register(Grupo)
admin.site.register(Seleccion)
admin.site.register(Ronda)
admin.site.register(Sede)
admin.site.register(Pronostico)
admin.site.register(Resultado)
admin.site.register(PartidoSeleccion)