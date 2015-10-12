# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0001_initial'),
        ('venues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='height',
            field=models.IntegerField(default=120),
        ),
        migrations.AddField(
            model_name='venue',
            name='tint',
            field=models.ForeignKey(default=None, blank=True, to='themes.Color'),
        ),
    ]
