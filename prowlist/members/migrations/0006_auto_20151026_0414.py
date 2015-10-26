# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='profile',
            field=models.OneToOneField(null=True, blank=True, to='members.Profile'),
        ),
        migrations.AlterField(
            model_name='member',
            name='token',
            field=models.OneToOneField(to='members.Token'),
        ),
        migrations.AlterField(
            model_name='member',
            name='user',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
