# Generated by Django 3.0.6 on 2020-06-10 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0025_remove_oraciosypeticiones_select_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OraciosYPeticiones',
            new_name='O_P',
        ),
    ]