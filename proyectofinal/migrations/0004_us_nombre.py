# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectofinal', '0003_auto_20161027_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='us',
            name='nombre',
            field=models.CharField(max_length=50, default=''),
            preserve_default=False,
        ),
    ]
