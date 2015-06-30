# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
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
            bases=(models.Model,),
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
            bases=(models.Model,),
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
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='variants',
            field=models.ManyToManyField(to='products.Variant', blank=True),
            preserve_default=True,
        ),
    ]
