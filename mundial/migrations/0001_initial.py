# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 05:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letra', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('jugado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pronostico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntos', models.IntegerField(default=0)),
                ('partido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mundial.Partido')),
            ],
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goles_local', models.IntegerField(default=None)),
                ('goles_visitante', models.IntegerField(default=None)),
                ('penales_local', models.IntegerField(default=None)),
                ('penales_visitante', models.IntegerField(default=None)),
                ('ganador_id', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Ronda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Seleccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('img_url', models.CharField(max_length=200)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mundial.Grupo')),
            ],
        ),
        migrations.AddField(
            model_name='pronostico',
            name='resultado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mundial.Resultado'),
        ),
        migrations.AddField(
            model_name='partido',
            name='resultado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mundial.Resultado'),
        ),
        migrations.AddField(
            model_name='partido',
            name='ronda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mundial.Ronda'),
        ),
        migrations.AddField(
            model_name='partido',
            name='sede',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mundial.Sede'),
        ),
    ]
