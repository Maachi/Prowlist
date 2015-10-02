# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(max_digits=20, decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'Variant choises',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(default=None, null=True, blank=True)),
                ('header_image', models.FileField(default=None, null=True, upload_to=products.models.upload_header_image, blank=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('point_contact_provider', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('point_contact_email', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('description', models.TextField(default=None, null=True, blank=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('locations', models.ManyToManyField(to='locations.Location', null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Products - Providers',
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('choise', models.ForeignKey(to='products.Choise')),
            ],
            options={
                'verbose_name_plural': 'Product variants',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='provider',
            field=models.ForeignKey(blank=True, to='products.Provider', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='tags.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='variants',
            field=models.ManyToManyField(to='products.Variant', blank=True),
        ),
    ]
