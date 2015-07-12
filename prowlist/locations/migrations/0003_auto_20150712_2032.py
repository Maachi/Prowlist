# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_remove_state_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='country',
        ),
        migrations.RemoveField(
            model_name='location',
            name='state',
        ),
    ]
