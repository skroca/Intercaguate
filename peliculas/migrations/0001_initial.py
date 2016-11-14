# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Actuacion',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('actor', models.ForeignKey(to='peliculas.Actor')),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('anio', models.IntegerField()),
                ('actores', models.ManyToManyField(through='peliculas.Actuacion', to='peliculas.Actor')),
            ],
        ),
        migrations.AddField(
            model_name='actuacion',
            name='pelicula',
            field=models.ForeignKey(to='peliculas.Pelicula'),
        ),
    ]
