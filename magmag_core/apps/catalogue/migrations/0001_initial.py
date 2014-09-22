# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
import magmag_core.apps.base_models.path_builder
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name', db_index=True)),
                ('description', models.TextField(blank=True, verbose_name='Description', null=True)),
                ('image', models.ImageField(upload_to='categories', blank=True, verbose_name='Image', null=True)),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(to='catalogue.Category', related_name='children', blank=True, null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
                'verbose_name': 'Category',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name', db_index=True)),
                ('description', models.TextField(blank=True, verbose_name='Description', null=True)),
                ('image', models.ImageField(upload_to=magmag_core.apps.base_models.path_builder.upload_to_product_path, blank=True, verbose_name='Image', null=True)),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
                ('date_added', models.DateField(default=datetime.datetime(2014, 9, 22, 20, 47, 25, 260626), verbose_name='Date_Added', editable=False)),
                ('article', models.CharField(max_length=10, default='', verbose_name='Article', db_index=True)),
                ('price', models.DecimalField(default=0, max_digits=8, verbose_name='Price', decimal_places=2)),
                ('hidden', models.BooleanField(default=False, verbose_name='Hidden')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Products',
                'ordering': ['name'],
                'verbose_name': 'Product',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('original', models.ImageField(upload_to=magmag_core.apps.base_models.path_builder.upload_to_image_product_path, verbose_name='Original')),
                ('preview', models.ImageField(upload_to=magmag_core.apps.base_models.path_builder.upload_to_image_product_path, verbose_name='Preview')),
                ('thumbnail', models.ImageField(upload_to=magmag_core.apps.base_models.path_builder.upload_to_image_product_path, verbose_name='Thumbnail')),
                ('caption', models.CharField(max_length=200, blank=True, verbose_name='Caption', null=True)),
                ('display_order', models.PositiveIntegerField(default=1, verbose_name='Display Order', help_text='An image with a display order of\n                       1 will be the primary image for a product')),
                ('date_created', models.DateTimeField(verbose_name='Date Created', auto_now_add=True)),
                ('product', models.ForeignKey(to='catalogue.Product', verbose_name='Product', related_name='images')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Product Images',
                'ordering': ['display_order'],
                'verbose_name': 'Product Image',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('color', models.CharField(max_length=64, verbose_name='Color', db_index=True)),
                ('size', models.CharField(max_length=5, verbose_name='Size', db_index=True)),
                ('product', models.ForeignKey(to='catalogue.Product', verbose_name='Product', related_name='items')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Items',
                'ordering': ['size'],
                'verbose_name': 'Item',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StockItem',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('count', models.PositiveIntegerField(default=0, verbose_name='Count')),
                ('product_item', models.ForeignKey(to='catalogue.ProductItem', verbose_name='ProductItem', related_name='stock_items')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'StockItems',
                'verbose_name': 'StockItem',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=64, verbose_name='Name', db_index=True)),
                ('phone', models.CharField(max_length=24, verbose_name='Phone')),
                ('address', models.CharField(max_length=256, verbose_name='Address')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Stores',
                'ordering': ['name'],
                'verbose_name': 'Store',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='stockitem',
            name='store',
            field=models.ForeignKey(to='catalogue.Store', verbose_name='Store', related_name='stock_items'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='stockitem',
            unique_together=set([('product_item', 'store')]),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([('slug', 'article')]),
        ),
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(blank=True, verbose_name='products', to='catalogue.Product', related_name='categories'),
            preserve_default=True,
        ),
    ]
