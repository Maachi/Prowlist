# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='friends',
            field=models.ManyToManyField(related_name='friends_rel_+', to='members.Member', blank=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='devices',
            field=models.ManyToManyField(to='members.Device', blank=True),
        ),
    ]
