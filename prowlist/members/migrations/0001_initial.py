# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import members.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client', models.TextField(null=True, blank=True)),
                ('platform', models.CharField(max_length=250, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Devices - Session devices',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cell_phone', models.CharField(max_length=250, null=True, blank=True)),
                ('terms_agreed', models.BooleanField(default=False, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('join_date', models.DateTimeField(null=True, blank=True)),
                ('validated_email', models.BooleanField(default=False, db_index=True)),
                ('validated_email_date', models.DateTimeField(null=True, blank=True)),
                ('validated_cell_phone_date', models.DateTimeField(null=True, blank=True)),
                ('friends', models.ManyToManyField(related_name='friends_rel_+', null=True, to='members.Member', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Members - Prowlist Application Users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(default=None, max_length=32, null=True, blank=True, choices=[(b'1', b'Male'), (b'2', b'Female')])),
                ('photo', models.FileField(default=None, null=True, upload_to=members.models.upload_photo_to, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Profile - Prowlist user Profile',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=250, null=True, blank=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('devices', models.ManyToManyField(to='members.Device', null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Token - Tokens or Sessions',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='member',
            name='profile',
            field=models.ForeignKey(blank=True, to='members.Profile', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='token',
            field=models.ForeignKey(to='members.Token'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
