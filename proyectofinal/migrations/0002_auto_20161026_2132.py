# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proyectofinal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Im',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='albums/Images/')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='tw',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Us',
        ),
        migrations.AddField(
            model_name='tw',
            name='id_tw',
            field=models.ForeignKey(to='proyectofinal.Im', null=True, blank=True),
        ),
    ]
