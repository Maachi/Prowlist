# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Venue Types',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='venue',
            name='types',
            field=models.ManyToManyField(to='venues.Type', blank=True),
            preserve_default=True,
        ),
    ]
