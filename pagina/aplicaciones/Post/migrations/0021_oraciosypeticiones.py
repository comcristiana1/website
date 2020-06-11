# Generated by Django 3.0.6 on 2020-06-10 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0020_merge_20200610_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='OraciosYPeticiones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_person', models.CharField(max_length=100, verbose_name='Nombre de la persona')),
                ('mail_persona', models.EmailField(max_length=30, verbose_name='Correo de la persona')),
                ('select_category', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=30, verbose_name='Titulo de Oración/Petición')),
                ('description', models.CharField(max_length=255, verbose_name='Descripción de la Oración/Petición')),
            ],
        ),
    ]
