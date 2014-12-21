__author__ = 'dimitriy'

from urllib import unquote
from django.views.generic import CreateView, DetailView, FormView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from magmag_core.apps.order.forms import CheckoutForm
from magmag_core.apps.order.models_logic import OrderCheckout
from magmag_core.global_utils.json import deserialize_list
from magmag_core.apps.catalogue.models import ProductItem
from magmag_core.apps.order.models import PurchaseItem, Order
from magmag_core.apps.base_models.defaults import MAGMAG_ORDER_STATUSES, MAGMAG_DELIVERY_METHODS, MAGMAG_DELIVERY_COSTS


class CheckoutView(FormView):
    template_name = 'order/checkout.html'
    form_class = CheckoutForm
    success_url = 'magmag:order:thank_you'
    process_form = OrderCheckout.process_form

    def __init__(self, *args, **kwargs):
        super(CheckoutView, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(CheckoutView, self).get_context_data(**kwargs)
        lst = deserialize_list(unquote(self.request.COOKIES['purchase_items'])) \
            if 'purchase_items' in self.request.COOKIES else list()
        pis = dict([(x['id'], x['count']) for x in lst])
        products = list(ProductItem.objects.select_related('product').filter(id__in=pis.keys()))

        form = kwargs.get('form', None)
        if form is not None:
            form.initial = {'json_purchase_pi': self.request.COOKIES['purchase_items'] if 'purchase_items' in self.request.COOKIES else ''}
            if hasattr(form, 'cleaned_data'):
                delivery_method = form.cleaned_data.get('delivery_method', None)
                if delivery_method:
                    ctx['delivery_cost'] = MAGMAG_DELIVERY_COSTS[delivery_method]
            else:
                ctx['delivery_cost'] = 0
        else:
            ctx['delivery_cost'] = 0

        ctx['total_sum'] = sum(el.product.price*pis[el.id] for el in products)+ctx['delivery_cost']

        if 'pi_items' not in ctx:
            ctx['pi_items'] = [PurchaseItem().initialize(pis[product.id], product) for product in products]

        ctx['delivery_taxes'] = [(k, v) for k, v in MAGMAG_DELIVERY_COSTS.items()]
        return ctx

    def form_valid(self, form):
        order_data = self.process_form(form)
        OrderCheckout.send_confirmation(order_data)
        return self.get_success_response(order_data)

    def get_success_response(self, order_data):
        return HttpResponseRedirect(self.get_success_url(order_data))

    def get_success_url(self, order_data):
        return reverse(self.success_url, args=(order_data[2].slug,))


class ThankYouView(DetailView):
    template_name = 'order/thank_you.html'
    model = Order
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        ctx = super(ThankYouView, self).get_context_data(**kwargs)
        items = list(self.object.items.select_related('product_item__product'))
        ctx['items'] = items
        return ctx