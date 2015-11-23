# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

from django.forms import ModelForm
from magmag_core.apps.order.models import Order


class OrderFullForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"


class OrderStatusForm(ModelForm):
    class Meta:
        model = Order
        exclude = ['number', 'date_created', 'slug', 'customer', 'total_sum', 'comment', 'delivery']
