# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0006_venue_sensors'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='member_rating',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='venue',
            name='star_rating',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
