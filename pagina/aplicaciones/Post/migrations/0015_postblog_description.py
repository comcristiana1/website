# Generated by Django 3.0.6 on 2020-06-27 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0014_auto_20200626_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='postblog',
            name='description',
            field=models.CharField(blank=True, max_length=200, verbose_name='Descripcion del Post'),
        ),
    ]
