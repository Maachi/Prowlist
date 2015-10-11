# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import members.models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20151011_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(default=None, null=True, upload_to=members.models.upload_avatar_to, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Avatars - Prowlist user Avatars',
            },
        ),
    ]
