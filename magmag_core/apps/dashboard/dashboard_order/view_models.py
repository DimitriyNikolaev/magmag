# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

from magmag_core.apps.base_models.defaults import MAGMAG_ORDER_STATUSES
from time import mktime


def get_order_model(view, order):
    return {
        'id': order.id,
        'status_id': MAGMAG_ORDER_STATUSES[order.status-1][0],
        'status_name': unicode(MAGMAG_ORDER_STATUSES[order.status-1][1]),#str(MAGMAG_ORDER_STATUSES[order.status-1][1]),
        'number': order.number,
        'date': order.date_created.strftime('%d.%m.%Y %H:%M'),
        'total_sum': float(order.total_sum),
        'customer_name': order.customer.name,
        'customer_email': order.customer.email
    }


def get_purchase_item_model(view, item):
    return {
        'id': item.id,
        'name': item.product_item.product.name,
        'size': item.product_item.size,
        'color': item.product_item.color,
        'count': item.count,
        'price': float(item.price)
    }


def get_client_request_model(view, item):
    return {
        'id': item.id,
        'viewed': item.viewed,
        'date': item.date.strftime('%d.%m.%Y %H:%M'),
        'email': item.email,
        'message': item.message
    }


def get_call_request_model(view, item):
    return {
        'id': item.id,
        'viewed': item.viewed,
        'date': item.date.strftime('%d.%m.%Y %H:%M'),
        'phone': item.phone,

    }