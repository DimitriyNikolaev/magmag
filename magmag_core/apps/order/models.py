__author__ = 'dimitriy'

from magmag_core.apps.base_models.base_order import AbstractOrder, AbstractPurchaseItem, AbstractReservation, AbstractDelivery


class Order(AbstractOrder):
    @property
    def identifier(self):
        return self.id if self.id is not None else 0

    @property
    def order_comment(self):
        return self.comment if self.comment is not None else ''


class Delivery(AbstractDelivery):
    pass


class PurchaseItem(AbstractPurchaseItem):
    def initialize(self, count, product_item):
        self.price = product_item.product.price
        self.count = count
        self.product_item = product_item
        return self


class Reservation(AbstractReservation):
    pass