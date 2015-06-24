# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20150623_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='user',
        ),
        migrations.AddField(
            model_name='token',
            name='member',
            field=models.ForeignKey(blank=True, to='members.Member', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='token',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
    ]
