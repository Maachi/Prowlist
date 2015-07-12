# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='alpha',
            field=models.DecimalField(default=0, max_digits=1, decimal_places=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='color',
            name='blue',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='color',
            name='green',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='color',
            name='red',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
