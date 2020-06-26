# Generated by Django 3.0.7 on 2020-06-26 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0009_contactos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edificadores',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipe', models.CharField(max_length=15, verbose_name='Tipo')),
                ('name', models.CharField(max_length=80, verbose_name='Nombre')),
                ('mail', models.EmailField(max_length=50, verbose_name='Email')),
                ('description', models.CharField(max_length=200, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Edificadores',
                'verbose_name_plural': 'Edificadores',
            },
        ),
    ]
