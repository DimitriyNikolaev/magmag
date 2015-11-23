# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallRequest',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Date', auto_now_add=True)),
                ('viewed', models.BooleanField(default=False, verbose_name='Viewed')),
                ('phone', models.CharField(max_length=16, verbose_name='Phone')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClientRequest',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Date', auto_now_add=True)),
                ('viewed', models.BooleanField(default=False, verbose_name='Viewed')),
                ('message', models.TextField(verbose_name='Message')),
                ('email', models.EmailField(max_length=75, verbose_name='Email')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
