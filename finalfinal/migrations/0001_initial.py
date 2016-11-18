# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('editorial', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('isbn', models.CharField(max_length=13)),
                ('titulo', models.TextField()),
                ('autor', models.TextField()),
                ('año', models.IntegerField()),
                ('fecha_prestamo', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('pais', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('dpi', models.IntegerField(max_length=13)),
                ('nombre', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='libro',
            name='prestamista',
            field=models.ForeignKey(null=True, blank=True, to='finalfinal.Usuario'),
        ),
    ]
