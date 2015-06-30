# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
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
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name_plural': 'Profile - Prowlist user Profile'},
        ),
        migrations.AlterModelOptions(
            name='token',
            options={'verbose_name_plural': 'Token - Tokens or Sessions'},
        ),
        migrations.RemoveField(
            model_name='token',
            name='client',
        ),
        migrations.AddField(
            model_name='token',
            name='devices',
            field=models.ManyToManyField(to='members.Device', null=True, blank=True),
            preserve_default=True,
        ),
    ]
