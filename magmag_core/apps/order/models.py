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
    pass


class Reservation(AbstractReservation):
    pass