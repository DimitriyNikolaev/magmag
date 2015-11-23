# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

from magmag_core.apps.base_models.base_models import AbstractCategory, AbstractStore, AbstractProduct, \
    AbstractProductImage, AbstractProductItem, AbstractStockItem


class Category(AbstractCategory):
    pass


class Store(AbstractStore):
    pass


class Product(AbstractProduct):
    pass


class ProductImage(AbstractProductImage):
    pass


class ProductItem(AbstractProductItem):

    @property
    def hash_name(self):
        return str(hash(self.color)).replace('-', '_') + str(hash(self.size)).replace('-', '_')

    def total_count(self):
        return sum(res.count for res in self.stock_items.all())


class StockItem(AbstractStockItem):

    @property
    def total_count(self):
        return self.count - sum(res.count for res in self.reservation.all())

