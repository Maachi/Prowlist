# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20150629_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='user',
        ),
        migrations.AlterField(
            model_name='member',
            name='terms_agreed',
            field=models.BooleanField(default=False, db_index=True),
            preserve_default=True,
        ),
    ]
