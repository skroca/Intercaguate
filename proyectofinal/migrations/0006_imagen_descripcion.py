# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectofinal', '0005_auto_20161114_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagen',
            name='descripcion',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
