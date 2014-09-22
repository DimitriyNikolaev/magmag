__author__ = 'dimitriy'

from django.views.generic import CreateView, TemplateView
from magmag_core.apps.order.forms import ProfileForm, AddressInlineFormset, OrderInlineFormset


class CheckoutView(CreateView):
    template_name = 'order/checkout.html'
    form_class = ProfileForm

    def get_context_data(self, **kwargs):
        ctx = super(CheckoutView, self).get_context_data(**kwargs)
        if 'address_formset' not in ctx:
            ctx['address_formset'] = AddressInlineFormset()
        if 'order_formset' not in ctx:
            ctx['order_formset'] = OrderInlineFormset()
        return ctx


class ThankYouView(TemplateView):
    template_name = 'order/thankyou.html'