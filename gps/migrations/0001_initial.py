# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 14:36
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Databasechangeloglock',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('locked', models.BooleanField()),
                ('lockgranted', models.DateTimeField(blank=True, null=True)),
                ('lockedby', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'databasechangeloglock',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration', models.BooleanField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('zoom', models.IntegerField()),
                ('map', models.CharField(blank=True, max_length=128, null=True)),
                ('language', models.CharField(blank=True, max_length=128, null=True)),
                ('distanceunit', models.CharField(blank=True, db_column='distanceUnit', max_length=128, null=True)),
                ('speedunit', models.CharField(blank=True, db_column='speedUnit', max_length=128, null=True)),
                ('bingkey', models.CharField(blank=True, db_column='bingKey', max_length=128, null=True)),
                ('mapurl', models.CharField(blank=True, db_column='mapUrl', max_length=128, null=True)),
                ('readonly', models.BooleanField()),
            ],
            options={
                'db_table': 'server',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'user_device',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128, unique=True)),
                ('hashedpassword', models.CharField(db_column='hashedPassword', max_length=128)),
                ('salt', models.CharField(max_length=128)),
                ('readonly', models.BooleanField()),
                ('admin', models.BooleanField()),
                ('map', models.CharField(blank=True, max_length=128, null=True)),
                ('language', models.CharField(blank=True, max_length=128, null=True)),
                ('distanceunit', models.CharField(blank=True, db_column='distanceUnit', max_length=128, null=True)),
                ('speedunit', models.CharField(blank=True, db_column='speedUnit', max_length=128, null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('zoom', models.IntegerField()),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CentroNegocios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=128, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('uniqueid', models.CharField(db_column='uniqueId', max_length=128, unique=True)),
                ('status', models.CharField(blank=True, max_length=128, null=True)),
                ('lastupdate', models.DateTimeField(blank=True, db_column='lastUpdate', null=True)),
                ('positionid', models.IntegerField(blank=True, db_column='positionId', null=True)),
            ],
            options={
                'db_table': 'devices',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=128, null=True)),
                ('empresa', models.CharField(blank=True, max_length=128, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devicetime', models.DateTimeField(db_column='deviceTime')),
                ('valid', models.BooleanField()),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('address', models.CharField(blank=True, max_length=512, null=True)),
                ('attributes', models.CharField(max_length=4096)),
                ('geom', django.contrib.gis.db.models.fields.PointField(db_column='punto', default='SRID=4326;POINT(0.0 0.0)', srid=4326)),
                ('deviceid', models.ForeignKey(db_column='deviceId', on_delete=django.db.models.deletion.DO_NOTHING, to='gps.Devices')),
            ],
            options={
                'db_table': 'pos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=128, null=True)),
                ('centroNegocios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gps.CentroNegocios')),
            ],
        ),
        migrations.AddField(
            model_name='centronegocios',
            name='planta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gps.Planta'),
        ),
    ]
