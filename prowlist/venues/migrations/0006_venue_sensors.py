# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0001_initial'),
        ('venues', '0005_auto_20150721_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='sensors',
            field=models.ManyToManyField(to='sensors.Sensor', blank=True),
            preserve_default=True,
        ),
    ]
