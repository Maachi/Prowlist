# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0002_auto_20151012_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='address',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='controller_style',
            field=models.CharField(default=None, max_length=32, null=True, blank=True, choices=[(b'1', b'ProwlistControllerStyleDefault'), (b'2', b'ProwlistControllerStyleLight')]),
        ),
        migrations.AlterField(
            model_name='venue',
            name='tint',
            field=models.ForeignKey(to='themes.Color', blank=True),
        ),
    ]
