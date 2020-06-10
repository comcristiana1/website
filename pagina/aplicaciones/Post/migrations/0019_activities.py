# Generated by Django 3.0.6 on 2020-06-10 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0018_auto_20200610_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('actName', models.CharField(max_length=40, verbose_name='Nombre Actividad')),
                ('actPhoto', models.ImageField(upload_to='activ_image', verbose_name='Imagen Actividad')),
                ('actDesc', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripcion')),
                ('actDate', models.DateField(verbose_name='Fecha Actividad')),
                ('actTimei', models.TimeField(verbose_name='Hora Inicio')),
                ('actTimef', models.TimeField(verbose_name='Hora Fin')),
                ('actDir', models.CharField(max_length=100, verbose_name='Dirección')),
                ('actPers', models.CharField(max_length=60, verbose_name='Encargado')),
                ('actPhono', models.CharField(blank=True, max_length=10, null=True, verbose_name='Teléfono Celular ')),
                ('actPhono2', models.CharField(blank=True, max_length=10, null=True, verbose_name='Teléfono Convencional ')),
                ('actMail', models.EmailField(blank=True, max_length=30, null=True, unique=True, verbose_name='Correo Electrónico ')),
                ('actStatus', models.BooleanField(default=True, verbose_name='Estado Activado/Desactivado')),
            ],
            options={
                'verbose_name': 'Actividades',
                'verbose_name_plural': 'Actividades',
            },
        ),
    ]
