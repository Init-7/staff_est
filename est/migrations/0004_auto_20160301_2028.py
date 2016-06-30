# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('est', '0003_trabajador_nota'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajador',
            name='nota2',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='tipo_contacto',
            field=models.CharField(blank=True, choices=[('PADRE', 'Padre'), ('MADRE', 'Madre'), ('ESPOSO', 'Esposa(o)'), ('ABUELO', 'Abuelo(a)'), ('HIJO', 'Hijo(a)'), ('PAREJA', 'Pareja')], max_length=128, null=True),
        ),
    ]
