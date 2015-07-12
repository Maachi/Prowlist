# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0002_auto_20150712_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='brand',
            field=models.ForeignKey(to='venues.Brand'),
            preserve_default=True,
        ),
    ]
