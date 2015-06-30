# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('red', models.DecimalField(max_digits=3, decimal_places=1)),
                ('green', models.DecimalField(max_digits=3, decimal_places=1)),
                ('blue', models.DecimalField(max_digits=3, decimal_places=1)),
            ],
            options={
                'verbose_name_plural': 'Colors',
            },
            bases=(models.Model,),
        ),
    ]
