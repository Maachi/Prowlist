# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('venues', '0004_venue_products_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='value',
            field=models.CharField(default=None, max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='venue',
            name='tags',
            field=models.ManyToManyField(to='tags.Tag', blank=True),
            preserve_default=True,
        ),
    ]
