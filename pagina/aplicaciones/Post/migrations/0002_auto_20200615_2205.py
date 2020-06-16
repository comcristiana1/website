# Generated by Django 3.0.6 on 2020-06-16 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40, verbose_name='Nombre Actividad')),
                ('activity_image', models.ImageField(blank=True, upload_to='activ_image', verbose_name='Imagen Actividad')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripcion')),
                ('date', models.DateField(verbose_name='Fecha Actividad')),
                ('initial_hour', models.TimeField(verbose_name='Hora Inicio')),
                ('finish_hour', models.TimeField(verbose_name='Hora Fin')),
                ('direction', models.CharField(max_length=100, verbose_name='Dirección')),
                ('in_charge', models.CharField(max_length=60, verbose_name='Encargado')),
                ('phone1', models.CharField(blank=True, max_length=10, null=True, verbose_name='Teléfono Celular ')),
                ('phone2', models.CharField(blank=True, max_length=10, null=True, verbose_name='Teléfono Convencional ')),
                ('mail', models.EmailField(blank=True, max_length=30, null=True, unique=True, verbose_name='Correo Electrónico ')),
                ('status', models.BooleanField(default=True, verbose_name='Estado Activado/Desactivado')),
            ],
            options={
                'verbose_name': 'Actividades',
                'verbose_name_plural': 'Actividades',
            },
        ),
        migrations.DeleteModel(
            name='Activities',
        ),
        migrations.RenameField(
            model_name='miembro',
            old_name='miemCrea',
            new_name='creation_date',
        ),
        migrations.RenameField(
            model_name='miembro',
            old_name='miemDesc',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='miembro',
            old_name='miemName1',
            new_name='name1',
        ),
        migrations.RenameField(
            model_name='miembro',
            old_name='miemName2',
            new_name='name2',
        ),
        migrations.RenameField(
            model_name='miembro',
            old_name='miemOcu',
            new_name='ocupation',
        ),
        migrations.RenameField(
            model_name='miembro',
            old_name='miemPho1',
            new_name='phone1',
        ),
        migrations.RenameField(
            model_name='miembro',
            old_name='miemPho2',
            new_name='phone2',
        ),
        migrations.RenameField(
            model_name='miembro',
            old_name='miemSurname1',
            new_name='surname1',
        ),
        migrations.RenameField(
            model_name='miembro',
            old_name='miemSurname2',
            new_name='surname2',
        ),
        migrations.AddField(
            model_name='miembro',
            name='member_image',
            field=models.ImageField(blank=True, upload_to='member_image', verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='miembro',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Estado Publicado/No_Publicado'),
        ),
    ]
