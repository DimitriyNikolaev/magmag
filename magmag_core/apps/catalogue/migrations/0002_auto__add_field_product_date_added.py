# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.date_added'
        db.add_column('catalogue_product', 'date_added',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 11, 24, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Product.date_added'
        db.delete_column('catalogue_product', 'date_added')


    models = {
        'catalogue.category': {
            'Meta': {'object_name': 'Category', 'ordering': "['name']"},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'to': "orm['catalogue.Category']", 'null': 'True', 'related_name': "'children'"}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['catalogue.Product']", 'symmetrical': 'False', 'related_name': "'categories'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'catalogue.product': {
            'Meta': {'object_name': 'Product', 'ordering': "['name']"},
            'date_added': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 11, 24, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        },
        'catalogue.productimage': {
            'Meta': {'object_name': 'ProductImage', 'unique_together': "(('product', 'display_order'),)", 'ordering': "['display_order']"},
            'caption': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
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
            'color': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': "orm['catalogue.Product']"}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '5', 'db_index': 'True'})
        },
        'catalogue.reservation': {
            'Meta': {'object_name': 'Reservation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reserve': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'stock_item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reservation'", 'to': "orm['catalogue.StockItem']"})
        },
        'catalogue.stockitem': {
            'Meta': {'object_name': 'StockItem'},
            'count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product_item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stock_items'", 'to': "orm['catalogue.ProductItem']"}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stock_items'", 'to': "orm['catalogue.Store']"})
        },
        'catalogue.store': {
            'Meta': {'object_name': 'Store', 'ordering': "['name']"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '24'})
        }
    }

    complete_apps = ['catalogue']