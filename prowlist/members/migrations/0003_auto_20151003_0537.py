# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import members.models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20151002_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default=None, null=True, upload_to=members.models.upload_photo_to, blank=True),
        ),
    ]
