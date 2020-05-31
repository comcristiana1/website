# Generated by Django 3.0.6 on 2020-05-30 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0004_auto_20200530_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Miembro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('miemName1', models.CharField(max_length=30, verbose_name='Primer Nombre')),
                ('miemName2', models.CharField(blank=True, max_length=30, null=True, verbose_name='Segundo Nombre')),
                ('miemSurname1', models.CharField(max_length=30, verbose_name='Primer Apellido')),
                ('miemSurname2', models.CharField(blank=True, max_length=30, null=True, verbose_name='Segundo Apellido')),
                ('miemOcu', models.CharField(max_length=30, verbose_name='Ocupación')),
                ('miemPho1', models.CharField(blank=True, max_length=10, null=True, verbose_name='Teléfono Convencional')),
                ('miemPho2', models.CharField(blank=True, max_length=10, null=True, verbose_name='Teléfono Celular')),
                ('miemCrea', models.DateField(default=datetime.datetime(2020, 5, 30, 11, 41, 29, 319312), verbose_name='Fecha de Creación')),
                ('miemDesc', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Miembro',
                'verbose_name_plural': 'Miembros',
            },
        ),
    ]
