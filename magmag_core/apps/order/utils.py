# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

from magmag_core.apps.order.models import Order


def get_new_order_number():
    return 1116 + Order.objects.count()
