__author__ = 'dimitriy'

from django.views.generic import CreateView, TemplateView, FormView

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from magmag_core.apps.order.forms import CheckoutForm
from magmag_core.apps.order.models_logic import OrderCheckout


class CheckoutView(FormView):
    template_name = 'order/checkout.html'
    form_class = CheckoutForm
    success_url = 'magmag:order:thank_you'
    process_form = OrderCheckout.process_form

    def __init__(self, *args, **kwargs):
        super(CheckoutView, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(CheckoutView, self).get_context_data(**kwargs)

        return ctx

    def form_valid(self, form):
        order_data = self.process_form(form)
        OrderCheckout.send_confirmation(order_data)
        return self.get_success_response(order_data)

    def get_success_response(self, order_data):
        return HttpResponseRedirect(self.get_success_url(order_data))

    def get_success_url(self, order_data):
        return reverse(self.success_url, args=(order_data[2].slug,))


class ThankYouView(TemplateView):
    template_name = 'order/thankyou.html'