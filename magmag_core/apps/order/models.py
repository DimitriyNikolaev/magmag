__author__ = 'dimitriy'

from magmag_core.apps.base_models.base_order import AbstractOrder, AbstractPurchaseItem, AbstractReservation


class Order(AbstractOrder):
    pass


class PurchaseItem(AbstractPurchaseItem):
    pass


class Reservation(AbstractReservation):
    pass