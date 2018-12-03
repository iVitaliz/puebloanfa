# Generated by Django 2.1.2 on 2018-12-03 16:34

from django.db import migrations, models
import django.db.models.aggregates


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='')),
                ('series', models.IntegerField()),
                ('futbolistas_inscritos', models.IntegerField()),
                ('pto_general', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='jugador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('goles', models.IntegerField()),
                ('tja_amarilla', models.IntegerField()),
                ('tja_roja', models.IntegerField()),
                ('estado', models.CharField(choices=[('expulsado', 'disponible')], max_length=200)),
                ('club', models.ForeignKey(on_delete=django.db.models.aggregates.Aggregate, to='anfa.club')),
            ],
        ),
    ]
