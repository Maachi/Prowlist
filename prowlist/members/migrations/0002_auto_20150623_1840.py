# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 23, 18, 40, 50, 57086)),
            preserve_default=True,
        ),
    ]
