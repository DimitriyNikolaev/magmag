# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

from django import forms
from django.forms.models import inlineformset_factory
from magmag_core.apps.order.models import Order
from magmag_core.apps.account.models import Profile, Address

from django import forms
from django.forms.util import ErrorList
from django.utils.translation import ugettext_lazy as _
from magmag_core.apps.base_models.defaults import MAGMAG_DELIVERY_METHODS
from magmag_core.global_utils.json import deserialize_list
from urllib import unquote
from magmag_core.apps.order.models import Order


class CheckoutForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': u'mail@example.com'}))
    phone = forms.CharField(required=False, label=_('Phone'),
                            widget=forms.TextInput(attrs={'placeholder': u'+7(911)-275-76-55'}))
    name = forms.CharField(required=True, label=_('Name'),
                           widget=forms.TextInput(attrs={'placeholder': _(u'Input your name')}))
    postal_code = forms.CharField(required=False, label=_('Postal code'),
                                  widget=forms.TextInput(attrs={'placeholder': u'123456'}))
    address = forms.CharField(required=False, label=_('Address'),
                              widget=forms.Textarea(attrs={'placeholder': u'г. Москва, ул. Профсоюзная, д.32, кв. 170 или м. Невский проспект'}))
    receiver_name = forms.CharField(required=False, label=_('Receiver name'),
                                    widget=forms.TextInput(
                                        attrs={'placeholder': u'Заполните, если получатель-другое лицо'}))
    delivery_method = forms.TypedChoiceField(required=True, coerce=int, label=_('Delivery method'),
                                             choices=MAGMAG_DELIVERY_METHODS,
                                             widget=forms.RadioSelect(attrs={'class': 'hidden'}), initial=3)
    comment = forms.CharField(required=False, label=_('Comment'),
                              widget=forms.Textarea(attrs={'placeholder': u'комментарии для магазина или курьера'}))
    json_purchase_pi = forms.CharField(widget=forms.HiddenInput(attrs={'id': u'json_purchase_pi'}))

    def clean(self):
        cleaned_data = super(CheckoutForm, self).clean()
        delivery_method = cleaned_data.get('delivery_method', None)
        msg = _('This field is required.')
        if delivery_method == 1 or delivery_method == 2 or delivery_method is None:
            code = cleaned_data.get('postal_code', None)
            address = cleaned_data.get('address', None)
            if code is None or code == '':
                #self.add_error('postal_code', msg) # django 1.7
                self.errors['postal_code'] = ErrorList([msg])
            if address is None or address == '':
                #self.add_error('address', msg) # django 1.7
                self.errors['address'] = ErrorList([msg])
        if delivery_method == 3 or delivery_method == 4:
            phone = cleaned_data.get('phone', None)
            if phone is None or phone == '':
                self.errors['phone'] = ErrorList([msg])
        if delivery_method == 4:
            address = cleaned_data.get('address', None)
            if address is None or address == '':
                #self.add_error('address', msg) # django 1.7
                self.errors['address'] = ErrorList([msg])

        lst = deserialize_list(unquote(cleaned_data['json_purchase_pi'])) if 'json_purchase_pi' in cleaned_data else list()
        if not lst:
            self.errors['json_purchase_pi'] = ErrorList([_(u'Add product to cart')])

        return cleaned_data