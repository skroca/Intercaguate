# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import proyectofinal.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('comentario', models.TextField()),
                ('fec', models.DateTimeField(default=django.utils.timezone.now)),
                ('fec_mod', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('fecha_pub', models.DateTimeField()),
                ('img', models.ImageField(width_field='width_field', height_field='height_field', null=True, blank=True, upload_to=proyectofinal.models.upload_location)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('usuario', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comentarios',
            name='id_comentario',
            field=models.ForeignKey(to='proyectofinal.Imagen'),
        ),
    ]
