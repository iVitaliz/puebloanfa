# Generated by Django 2.1.2 on 2018-12-03 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anfa', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='club',
            old_name='nombre',
            new_name='nombre_club',
        ),
        migrations.RenameField(
            model_name='jugador',
            old_name='nombre',
            new_name='nombre_jug',
        ),
    ]