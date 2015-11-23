# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import magmag_core.apps.pages.utils


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(default='Title', verbose_name='Title', max_length=255)),
                ('url', models.CharField(default='/', verbose_name='URL', max_length=255)),
                ('display_name', models.CharField(default='page', verbose_name='Display name', max_length=128)),
                ('content', models.TextField(blank=True, verbose_name='Content')),
                ('deletable', models.BooleanField(default=True, verbose_name='Deletable')),
                ('slug', models.SlugField(verbose_name='Slug', blank=True, null=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('image', models.ImageField(verbose_name='Image', upload_to=magmag_core.apps.pages.utils.upload_to_image_page_path)),
                ('caption', models.CharField(verbose_name='Caption', blank=True, null=True, max_length=200)),
                ('page', models.ForeignKey(to='pages.Page', verbose_name='Page', related_name='images')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
