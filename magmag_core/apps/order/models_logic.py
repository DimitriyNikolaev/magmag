# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

import datetime
import uuid
#from urllib.request import unquote
from urllib import unquote
from magmag_core.apps.order.models import PurchaseItem, Order, Delivery
from magmag_core.apps.account.models import Profile, Address
from magmag_core.apps.catalogue.models import Product
from magmag_core.apps.order.utils import get_new_order_number
from magmag_core.global_utils.json import deserialize_list
from magmag_core.global_utils.email import send_email
from magmag_core.apps.base_models.models_logic_base import BaseLogic
#from magmag_core.apps.base_models.defaults import MAGMAG_DELIVERY_COSTS

from django.template.loader import get_template
from django.template import Context
from django.utils.translation import ugettext_lazy as _


class OrderCheckout(object):
    @staticmethod
    def process_form(view, form):
        # lst = deserialize_list(unquote(form.cleaned_data['json_purchase_pi'])) if 'json_purchase_pi' in form.cleaned_data else list()
        # pis = dict([(x['id'], x['count']) for x in lst])
        # products = list(Product.objects.filter(id__in=pis.keys()))
        # total_sum = sum(el.price*pis[el.id] for el in products)

        customer = Profile()
        customer.name = form.cleaned_data['name']
        customer.email = form.cleaned_data['email']
        customer.phone = form.cleaned_data['phone']
        customer.is_subscribe = True
        #customer.save()
        address = Address()
        address.postal_code = form.cleaned_data['postal_code']
        address.address = form.cleaned_data['address']
        address.name = form.cleaned_data['receiver_name']
        if address.name is None or address.name == '':
            address.name = customer.name
        address.profile = customer
        #address.save()

        delivery = Delivery()
        delivery.delivery_method = form.cleaned_data['delivery_method']
        #delivery.cost = MAGMAG_DELIVERY_COSTS[delivery.delivery_method]
        delivery.address = address
        #delivery.save()


        order = Order()
        order.customer = customer
        order.delivery = delivery
        order.comment = form.cleaned_data['comment'] if len(form.cleaned_data['comment']) > 0 else None
        order.number = get_new_order_number()
        order.slug = uuid.uuid1().hex
        order.date_created = datetime.datetime.now()
        order.status = 1
        #order.total_sum = total_sum + delivery.cost
        #order.save()

        # pi_list = []
        # for prod in products:
        #     pi = PurchaseItem().initialize(count=pis[prod.id], product=prod)
        #     order.items.add(pi)
        #     pi_list.append(pi)


        return customer, address, order, delivery#, pi_list

    @staticmethod
    def send_confirmation(order_data):
        msg = get_template('order/checkout_email.txt').render(Context({
            'order': order_data[2],
            'delivery': order_data[3],
            'customer': order_data[0],
            'address': order_data[1],
            'items': order_data[4]
        }))
        #title = '%s № %s' % (str(_('Order')), order_data[2].number,)
        title = u'%s № %s' % (unicode(_('Order')), order_data[2].number,)
        send_email(title, msg, [order_data[0].email])


class OrderLogic(BaseLogic):
    pass