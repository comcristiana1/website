# Generated by Django 3.0.6 on 2020-06-10 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0026_auto_20200610_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='o_p',
            name='section_category',
            field=models.CharField(choices=[('Oracion', 'Oracion'), ('Peticion', 'Peticion')], default='Oracion', max_length=100),
        ),
    ]