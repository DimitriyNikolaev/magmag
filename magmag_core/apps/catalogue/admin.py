# -*- coding: utf-8 -*-
__author__ = 'dimitriy'
from django.contrib import admin
from magmag_core.apps.catalogue.models import Category, Store, Product

admin.site.register(Category)
admin.site.register(Store)
admin.site.register(Product)