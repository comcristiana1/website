# Generated by Django 3.0.6 on 2020-06-24 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_auto_20200616_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='category',
            field=models.CharField(choices=[(1, 'Espirituales'), (2, 'Sociales')], default=1, max_length=30, verbose_name='Categoria'),
        ),
    ]