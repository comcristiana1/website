# Generated by Django 3.0.7 on 2020-06-27 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0013_auto_20200626_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ministry',
            name='description',
            field=models.CharField(blank=True, max_length=800, verbose_name='Descripción'),
        ),
    ]
