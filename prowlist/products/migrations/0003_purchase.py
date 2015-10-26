# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_avatar'),
        ('products', '0002_auto_20151002_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('member', models.ForeignKey(to='members.Member')),
                ('product', models.ForeignKey(to='products.Product')),
            ],
            options={
                'verbose_name_plural': 'Member Purchases',
            },
        ),
    ]
