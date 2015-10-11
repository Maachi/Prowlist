# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import members.models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20151003_0537'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default=None, null=True, upload_to=members.models.upload_photo_to, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
