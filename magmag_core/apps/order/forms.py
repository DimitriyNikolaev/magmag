__author__ = 'dimitriy'

from django import forms
from django.forms.models import inlineformset_factory
from magmag_core.apps.order.models import Order
from magmag_core.apps.account.models import Profile, Address


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('comment',)

    def save(self, user):
            pass


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('total_sum',)


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address

BaseAddressInlineFormSet = inlineformset_factory(Profile, Address, AddressForm, can_delete=False, extra=1)


class AddressInlineFormset(BaseAddressInlineFormSet):
    pass

BaseOrderInlineFormSet = inlineformset_factory(Profile, Order, OrderForm, can_delete=False, extra=1)


class OrderInlineFormset(BaseOrderInlineFormSet):
    pass
