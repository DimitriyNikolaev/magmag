# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('catalogue_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=100, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(null=True, related_name='children', to=orm['catalogue.Category'], blank=True)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('catalogue', ['Category'])

        # Adding M2M table for field products on 'Category'
        m2m_table_name = db.shorten_name('catalogue_category_products')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('category', models.ForeignKey(orm['catalogue.category'], null=False)),
            ('product', models.ForeignKey(orm['catalogue.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['category_id', 'product_id'])

        # Adding model 'Store'
        db.create_table('catalogue_store', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=64)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=24)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('catalogue', ['Store'])

        # Adding model 'Product'
        db.create_table('catalogue_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=100, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
        ))
        db.send_create_signal('catalogue', ['Product'])

        # Adding model 'ProductImage'
        db.create_table('catalogue_productimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['catalogue.Product'])),
            ('original', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('preview', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.CharField')(null=True, max_length=200, blank=True)),
            ('display_order', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('catalogue', ['ProductImage'])

        # Adding unique constraint on 'ProductImage', fields ['product', 'display_order']
        db.create_unique('catalogue_productimage', ['product_id', 'display_order'])

        # Adding model 'ProductItem'
        db.create_table('catalogue_productitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(related_name='items', to=orm['catalogue.Product'])),
            ('color', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=64)),
            ('size', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=5)),
        ))
        db.send_create_signal('catalogue', ['ProductItem'])

        # Adding model 'StockItem'
        db.create_table('catalogue_stockitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product_item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='stock_items', to=orm['catalogue.ProductItem'])),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(related_name='stock_items', to=orm['catalogue.Store'])),
            ('count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal('catalogue', ['StockItem'])

        # Adding model 'Reservation'
        db.create_table('catalogue_reservation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stock_item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reservation', to=orm['catalogue.StockItem'])),
            ('reserve', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal('catalogue', ['Reservation'])


    def backwards(self, orm):
        # Removing unique constraint on 'ProductImage', fields ['product', 'display_order']
        db.delete_unique('catalogue_productimage', ['product_id', 'display_order'])

        # Deleting model 'Category'
        db.delete_table('catalogue_category')

        # Removing M2M table for field products on 'Category'
        db.delete_table(db.shorten_name('catalogue_category_products'))

        # Deleting model 'Store'
        db.delete_table('catalogue_store')

        # Deleting model 'Product'
        db.delete_table('catalogue_product')

        # Deleting model 'ProductImage'
        db.delete_table('catalogue_productimage')

        # Deleting model 'ProductItem'
        db.delete_table('catalogue_productitem')

        # Deleting model 'StockItem'
        db.delete_table('catalogue_stockitem')

        # Deleting model 'Reservation'
        db.delete_table('catalogue_reservation')


    models = {
        'catalogue.category': {
            'Meta': {'object_name': 'Category', 'ordering': "['name']"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'related_name': "'children'", 'to': "orm['catalogue.Category']", 'blank': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['catalogue.Product']", 'symmetrical': 'False', 'related_name': "'categories'", 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'catalogue.product': {
            'Meta': {'object_name': 'Product', 'ordering': "['name']"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        },
        'catalogue.productimage': {
            'Meta': {'object_name': 'ProductImage', 'unique_together': "(('product', 'display_order'),)", 'ordering': "['display_order']"},
            'caption': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '64'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '24'})
        }
    }

    complete_apps = ['catalogue']