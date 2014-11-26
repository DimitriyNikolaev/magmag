__author__ = 'dimitriy'

from django.db import models
from django.utils.translation import ugettext_lazy as _
from magmag_core.apps.order.models import *
from magmag_core.apps.account.models import Profile, Address
from magmag_core.apps.catalogue.models import StockItem
from magmag_core.apps.base_models.defaults import MAGMAG_ORDER_STATUSES, MAGMAG_DELIVERY_METHODS


class AbstractOrder(models.Model):
    number = models.IntegerField(_("Number"), blank=False, null=False)
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)
    slug = models.CharField(_("Slug"), blank=False, null=False, max_length=32)
    status = models.PositiveSmallIntegerField(
        _("Status"), null=False, default=0, blank=False, choices=MAGMAG_ORDER_STATUSES)
    customer = models.ForeignKey(Profile, related_name='orders', verbose_name=_("Customer"))
    comment = models.TextField(_("Comment"), blank=True, null=True)
    total_sum = models.DecimalField(_("Total_Sum"), blank=False, null=False, default=0, max_digits=8, decimal_places=2)
    delivery = models.ForeignKey('Delivery', related_name='order', verbose_name=_('Delivery'), null=True)

    class Meta:
        abstract = True
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")


class AbstractDelivery(models.Model):
    delivery_method = models.PositiveSmallIntegerField(_("Delivery method"), null=False, default=3, blank=False,
                                                       choices=MAGMAG_DELIVERY_METHODS)
    cost = models.DecimalField(_("Delivery cost"), null=False, default=0, blank=False, max_digits=8, decimal_places=2)
    address = models.ForeignKey(Address, null=True, verbose_name=_("Delivery address"))

    class Meta:
        abstract = True
        verbose_name = _("Delivery")
        verbose_name_plural = _("Delivery")


class AbstractPurchaseItem(models.Model):
    order = models.ForeignKey('Order', related_name='items', verbose_name=_("Order"))
    product_item = models.ForeignKey('PurchaseItem', related_name='purchase_items', verbose_name=_("Product"))
    price = models.DecimalField(_("Price"), null=False, blank=False, default=0, max_digits=8, decimal_places=2)
    count = models.PositiveSmallIntegerField(_("Count"), blank=False, null=False, default=0)

    class Meta:
        abstract = True
        verbose_name = _("Purchase Item")
        verbose_name_plural = _("Purchase Items")


class AbstractReservation(models.Model):
    stock_item = models.ForeignKey(StockItem, related_name='reservation', verbose_name=_("StockItem"))
    reserve = models.PositiveIntegerField(_('Count'), default=0, null=False, blank=False, editable=True)
    purchase_item = models.ForeignKey('PurchaseItem', related_name='reservation', verbose_name=_("PurchaseItem"))

    class Meta:
        abstract = True

