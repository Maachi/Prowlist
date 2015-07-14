# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0003_auto_20150712_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='products_count',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
