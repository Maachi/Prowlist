# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import venues.models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('products', '0001_initial'),
        ('colors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('color', models.ForeignKey(to='colors.Color')),
            ],
            options={
                'verbose_name_plural': 'Venue Attributes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('logo', models.FileField(default=None, null=True, upload_to=venues.models.upload_logo_image, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Venue Brand',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('small_description', models.CharField(max_length=200)),
                ('description', models.TextField(default=None, null=True, blank=True)),
                ('image', models.FileField(default=None, null=True, upload_to=venues.models.upload_venue_image, blank=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('attributes', models.ManyToManyField(to='venues.Attribute', blank=True)),
                ('brand', models.ForeignKey(to='products.Choise')),
                ('location', models.ForeignKey(to='locations.Location')),
                ('products', models.ManyToManyField(to='products.Product', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Venues',
            },
            bases=(models.Model,),
        ),
    ]
