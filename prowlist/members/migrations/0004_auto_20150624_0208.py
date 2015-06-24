# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20150624_0153'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=250, null=True, blank=True)),
                ('client', models.TextField(null=True, blank=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('member', models.ForeignKey(blank=True, to='members.Member', null=True)),
            ],
            options={
                'verbose_name_plural': 'Members - Tokens or Sessions',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='token',
            name='member',
        ),
        migrations.DeleteModel(
            name='Token',
        ),
    ]
