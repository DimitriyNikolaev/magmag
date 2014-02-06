# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.price'
        db.add_column('catalogue_product', 'price',
                      self.gf('django.db.models.fields.DecimalField')(max_digits=5, default=0, decimal_places=2),
                      keep_default=False)

        # Adding field 'Product.hidden'
        db.add_column('catalogue_product', 'hidden',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Product.price'
        db.delete_column('catalogue_product', 'price')

        # Deleting field 'Product.hidden'
        db.delete_column('catalogue_product', 'hidden')


    models = {
        'catalogue.category': {
            'Meta': {'object_name': 'Category', 'ordering': "['name']"},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'to': "orm['catalogue.Category']", 'related_name': "'children'", 'null': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['catalogue.Product']", 'symmetrical': 'False', 'related_name': "'categories'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'catalogue.product': {
            'Meta': {'object_name': 'Product', 'unique_together': "(('slug', 'article'),)", 'ordering': "['name']"},
            'article': ('django.db.models.fields.CharField', [], {'default': "''", 'db_index': 'True', 'max_length': '10'}),
            'date_added': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 2, 6, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'default': '0', 'decimal_places': '2'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        },
        'catalogue.productimage': {
            'Meta': {'object_name': 'ProductImage', 'unique_together': "(('product', 'display_order'),)", 'ordering': "['display_order']"},
            'caption': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'display_order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'preview': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['catalogue.Product']"}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'catalogue.productitem': {
            'Meta': {'object_name': 'ProductItem', 'ordering': "['size']"},
            'color': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': "orm['catalogue.Product']"}),
            'size': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '5'})
        },
        'catalogue.reservation': {
            'Meta': {'object_name': 'Reservation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reserve': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'stock_item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reservation'", 'to': "orm['catalogue.StockItem']"})
        },
        'catalogue.stockitem': {
            'Meta': {'object_name': 'StockItem', 'unique_together': "(('product_item', 'store'),)"},
            'count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product_item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stock_items'", 'to': "orm['catalogue.ProductItem']"}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stock_items'", 'to': "orm['catalogue.Store']"})
        },
        'catalogue.store': {
            'Meta': {'object_name': 'Store', 'ordering': "['name']"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '64'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '24'})
        }
    }

    complete_apps = ['catalogue']