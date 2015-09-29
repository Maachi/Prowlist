# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_location_name'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='locations',
            field=models.ManyToManyField(to='locations.Location', blank=True),
            preserve_default=True,
        ),
    ]
