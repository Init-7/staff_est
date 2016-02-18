# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 15:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('est', '0003_trabajador_gps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='centronegocios',
            name='geom',
        ),
        migrations.AddField(
            model_name='centronegocios',
            name='codigo',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='centronegocios',
            name='zonas',
            field=models.ManyToManyField(to='est.Zona'),
        ),
        migrations.AddField(
            model_name='trabajador',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='est.Trabajador'),
        ),
    ]
