# Generated by Django 3.0.6 on 2020-06-26 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0008_auto_20200624_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40, verbose_name='Nombre')),
                ('surname', models.CharField(max_length=40, verbose_name='Apellido')),
                ('mail', models.EmailField(max_length=40, unique=True, verbose_name='Correo Electrónico ')),
                ('message', models.TextField(verbose_name='Mensaje')),
                ('status', models.BooleanField(default=True, verbose_name='Estado Activado/Desactivado')),
            ],
            options={
                'verbose_name': 'Contactos',
                'verbose_name_plural': 'Contactos',
            },
        ),
    ]