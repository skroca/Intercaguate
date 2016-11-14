# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import proyectofinal.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proyectofinal', '0002_auto_20161026_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Us',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('img', models.ImageField(null=True, upload_to=proyectofinal.models.upload_location, blank=True, width_field='width_field', height_field='height_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='im',
            name='usuario',
        ),
        migrations.RenameField(
            model_name='tw',
            old_name='created_date',
            new_name='fec',
        ),
        migrations.AlterField(
            model_name='tw',
            name='id_tw',
            field=models.ForeignKey(to='proyectofinal.Us', default=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Im',
        ),
    ]
