__author__ = 'dimitriy'

from django.views.generic import CreateView, TemplateView


class CheckoutView(TemplateView):
    template_name = 'order/checkout.html'
