# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20150630_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='join_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
