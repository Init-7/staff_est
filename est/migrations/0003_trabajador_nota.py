# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('est', '0002_auto_20160229_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajador',
            name='nota',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
