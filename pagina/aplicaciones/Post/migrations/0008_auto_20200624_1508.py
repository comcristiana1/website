# Generated by Django 3.0.6 on 2020-06-24 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0007_auto_20200624_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='category',
            field=models.CharField(choices=[('Espirituales', 'Espirituales'), ('Sociales', 'Sociales')], max_length=30, verbose_name='Categoria'),
        ),
    ]