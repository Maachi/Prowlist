# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('uuid', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('serial', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('latitude', models.DecimalField(default=None, null=True, max_digits=20, decimal_places=17, blank=True)),
                ('longitude', models.DecimalField(default=None, null=True, max_digits=20, decimal_places=17, blank=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
            ],
            options={
                'verbose_name_plural': 'Sensors (Proximity detectors)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SensorLogs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=200)),
                ('validated_email_date', models.DateTimeField(null=True, blank=True)),
                ('sensor', models.ForeignKey(blank=True, to='sensors.Sensor', null=True)),
            ],
            options={
                'verbose_name_plural': 'Sensor Logs',
            },
            bases=(models.Model,),
        ),
    ]
