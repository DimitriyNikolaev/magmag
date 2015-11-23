# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_auto_20141218_2104'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('delivery_method', models.PositiveSmallIntegerField(verbose_name='Delivery method', choices=[(1, 'Post'), (2, 'EMS'), (3, 'Metro'), (4, 'Courier')], default=3)),
                ('cost', models.DecimalField(decimal_places=2, verbose_name='Delivery cost', max_digits=8, default=0)),
                ('address', models.ForeignKey(null=True, verbose_name='Delivery address', to='account.Address')),
            ],
            options={
                'verbose_name': 'Delivery',
                'verbose_name_plural': 'Delivery',
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('number', models.IntegerField(verbose_name='Number')),
                ('date_created', models.DateTimeField(verbose_name='Date Created', auto_now_add=True)),
                ('slug', models.CharField(verbose_name='Slug', max_length=32)),
                ('status', models.PositiveSmallIntegerField(verbose_name='Status', choices=[(1, 'Adopted'), (2, 'Paid'), (3, 'Completion'), (4, 'Completed'), (5, 'Sent')], default=0)),
                ('comment', models.TextField(blank=True, verbose_name='Comment', null=True)),
                ('total_sum', models.DecimalField(decimal_places=2, verbose_name='Total_Sum', max_digits=8, default=0)),
                ('customer', models.ForeignKey(related_name='orders', verbose_name='Customer', to='account.Profile')),
                ('delivery', models.ForeignKey(null=True, related_name='order', verbose_name='Delivery', to='order.Delivery')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('price', models.DecimalField(decimal_places=2, verbose_name='Price', max_digits=8, default=0)),
                ('count', models.PositiveSmallIntegerField(verbose_name='Count', default=0)),
                ('order', models.ForeignKey(related_name='items', verbose_name='Order', to='order.Order')),
                ('product_item', models.ForeignKey(related_name='purchase_items', verbose_name='Product', to='catalogue.ProductItem')),
            ],
            options={
                'verbose_name': 'Purchase Item',
                'verbose_name_plural': 'Purchase Items',
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('reserve', models.PositiveIntegerField(verbose_name='Count', default=0)),
                ('purchase_item', models.ForeignKey(related_name='reservation', verbose_name='PurchaseItem', to='order.PurchaseItem')),
                ('stock_item', models.ForeignKey(related_name='reservation', verbose_name='StockItem', to='catalogue.StockItem')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
