# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_auto_20140922_2052'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Number')),
                ('date_created', models.DateTimeField(verbose_name='Date Created', auto_now_add=True)),
                ('slug', models.CharField(max_length=32, verbose_name='Slug')),
                ('status', models.PositiveSmallIntegerField(default=0, choices=[(1, 'Adopted'), (2, 'Paid'), (3, 'Сompletion'), (4, 'Сompleted'), (5, 'Sent')], verbose_name='Status')),
                ('comment', models.TextField(blank=True, verbose_name='Comment', null=True)),
                ('total_sum', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Total_Sum')),
                ('customer', models.ForeignKey(related_name='orders', to='account.Profile', verbose_name='Customer')),
            ],
            options={
                'verbose_name_plural': 'Orders',
                'abstract': False,
                'verbose_name': 'Order',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Price')),
                ('count', models.PositiveSmallIntegerField(default=0, verbose_name='Count')),
                ('order', models.ForeignKey(related_name='items', to='order.Order', verbose_name='Order')),
                ('product_item', models.ForeignKey(related_name='purchase_items', to='order.PurchaseItem', verbose_name='Product')),
            ],
            options={
                'verbose_name_plural': 'Purchase Items',
                'abstract': False,
                'verbose_name': 'Purchase Item',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('reserve', models.PositiveIntegerField(default=0, verbose_name='Count')),
                ('purchase_item', models.ForeignKey(related_name='reservation', to='order.PurchaseItem', verbose_name='PurchaseItem')),
                ('stock_item', models.ForeignKey(related_name='reservation', to='catalogue.StockItem', verbose_name='StockItem')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
