# Generated by Django 3.0.6 on 2020-06-26 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0013_auto_20200626_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postblog',
            name='picture',
            field=models.ImageField(upload_to='Post'),
        ),
    ]
