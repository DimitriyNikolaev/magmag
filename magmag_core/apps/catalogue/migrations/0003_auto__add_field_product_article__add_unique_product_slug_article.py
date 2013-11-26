# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.article'
        db.add_column('catalogue_product', 'article',
                      self.gf('django.db.models.fields.CharField')(default='', db_index=True, max_length=10),
                      keep_default=False)

        # Adding unique constraint on 'Product', fields ['slug', 'article']
        db.create_unique('catalogue_product', ['slug', 'article'])


    def backwards(self, orm):
        # Removing unique constraint on 'Product', fields ['slug', 'article']
        db.delete_unique('catalogue_product', ['slug', 'article'])

        # Deleting field 'Product.article'
        db.delete_column('catalogue_product', 'article')


    models = {
        'catalogue.category': {
            'Meta': {'ordering': "['name']", 'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'related_name': "'children'", 'blank': 'True', 'to': "orm['catalogue.Category']", 'null': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['catalogue.Product']", 'related_name': "'categories'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'catalogue.product': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('slug', 'article'),)", 'object_name': 'Product'},
            'article': ('django.db.models.fields.CharField', [], {'default': "''", 'db_index': 'True', 'max_length': '10'}),
            'date_added': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 11, 24, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        },
        'catalogue.productimage': {
            'Meta': {'ordering': "['display_order']", 'unique_together': "(('product', 'display_order'),)", 'object_name': 'ProductImage'},
            'caption': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'display_order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'preview': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['catalogue.Product']"}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'catalogue.productitem': {
            'Meta': {'ordering': "['size']", 'object_name': 'ProductItem'},
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
            'Meta': {'object_name': 'StockItem'},
            'count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product_item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stock_items'", 'to': "orm['catalogue.ProductItem']"}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stock_items'", 'to': "orm['catalogue.Store']"})
        },
        'catalogue.store': {
            'Meta': {'ordering': "['name']", 'object_name': 'Store'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '64'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '24'})
        }
    }

    complete_apps = ['catalogue']