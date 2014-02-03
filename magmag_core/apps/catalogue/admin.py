# -*- coding: utf-8 -*-
__author__ = 'dimitriy'
from django.contrib import admin
from magmag_core.apps.catalogue.models import Category, Store, Product, ProductItem, ProductImage, StockItem

admin.site.register(Category)
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(ProductItem)
admin.site.register(StockItem)
admin.site.register(ProductImage)