# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import venues.models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0003_auto_20151013_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='logo_file',
            field=models.ImageField(default=None, null=True, upload_to=venues.models.upload_venue_image, blank=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=venues.models.upload_venue_image, blank=True),
        ),
    ]
