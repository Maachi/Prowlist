# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0002_auto_20150712_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='alpha',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
