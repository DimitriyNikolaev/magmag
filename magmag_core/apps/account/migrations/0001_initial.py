# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('postal_code', models.CharField(blank=True, max_length=6, verbose_name='Postal_Code', null=True)),
                ('address', models.CharField(blank=True, max_length=320, verbose_name='Address', null=True)),
                ('name', models.CharField(default='fio', max_length=80, verbose_name='Name')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('email', models.EmailField(unique=True, max_length=75, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=18, verbose_name='Phone', null=True)),
                ('total_sum', models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='Total_Sum')),
                ('name', models.CharField(default='fio', max_length=80, verbose_name='Name')),
                ('is_subscribe', models.BooleanField(default=True, verbose_name='Is_subscribe')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='address',
            name='profile',
            field=models.ForeignKey(to='account.Profile', related_name='addresses', verbose_name='Addresses'),
            preserve_default=True,
        ),
    ]
