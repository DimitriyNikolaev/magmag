# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

from magmag_core.apps.base_models.base_models import AbstractCategory, AbstractStore, AbstractProduct, \
    AbstractProductImage, AbstractProductItem, AbstractStockItem, AbstractReservation


class Category(AbstractCategory):
    pass


class Store(AbstractStore):
    pass


class Product(AbstractProduct):
    pass


class ProductImage(AbstractProductImage):
    pass


class ProductItem(AbstractProductItem):
    pass


class StockItem(AbstractStockItem):
    pass


class Reservation(AbstractReservation):
    pass
