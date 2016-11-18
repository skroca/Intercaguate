# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalfinal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='editorial',
            field=models.ForeignKey(null=True, to='finalfinal.Editorial'),
        ),
        migrations.AddField(
            model_name='libro',
            name='pais',
            field=models.ForeignKey(null=True, to='finalfinal.Pais'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='dpi',
            field=models.IntegerField(),
        ),
    ]
