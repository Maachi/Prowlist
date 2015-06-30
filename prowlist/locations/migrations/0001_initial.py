# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True, db_index=True)),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('prefix', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.DecimalField(default=None, null=True, max_digits=20, decimal_places=17, blank=True)),
                ('longitude', models.DecimalField(default=None, null=True, max_digits=20, decimal_places=17, blank=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('city', models.ForeignKey(to='locations.City')),
                ('country', models.ForeignKey(to='locations.Country')),
            ],
            options={
                'verbose_name_plural': 'Location',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('prefix', models.CharField(max_length=10, null=True, blank=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('country', models.ForeignKey(default=None, blank=True, to='locations.Country', null=True)),
            ],
            options={
                'verbose_name_plural': 'States',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.ForeignKey(blank=True, to='locations.State', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(to='locations.Country'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(blank=True, to='locations.State', null=True),
            preserve_default=True,
        ),
    ]
