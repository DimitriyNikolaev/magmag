# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

from magmag_core.view.base_views import SingleEditMixedView, ListMixedView, SingleTreeEditorMixin, SingleEditorMixin, \
    FormsetEditorMixin
from magmag_core.apps.order.models import Order
from magmag_core.apps.message.models import ClientRequest, CallRequest
from magmag_core.apps.dashboard.dashboard_order.view_models import get_order_model, get_purchase_item_model, \
    get_client_request_model, get_call_request_model
from magmag_core.apps.dashboard.dashboard_order.forms import OrderStatusForm
from magmag_core.apps.message.forms import CallRequestFullForm, ClientRequestFullForm
from magmag_core.apps.order.models_logic import OrderLogic
from magmag_core.apps.message.models_logic import MessageLogic
from magmag_core.global_utils.json import serialize_list
from magmag_core.apps.base_models.defaults import MAGMAG_ORDER_STATUSES
from magmag_core.apps.dashboard.common_view_models import get_key_name_model


class OrderListView(ListMixedView, SingleEditorMixin):
    template_name = 'dashboard/order/orders.html'
    model = Order
    context_object_name = 'order'
    converter = get_order_model
    paginate_by = 20

    def get_queryset(self):
        return Order.objects.select_related('customer').order_by('-date_created')

    def get_context_data(self, **kwargs):
        ctx = super(ListMixedView, self).get_context_data(**kwargs)
        ctx['page_size'] = self.paginate_by
        return ctx


class OrderFormView(SingleEditMixedView, SingleEditorMixin):
    template_name = 'dashboard/order/order_form.html'
    model = Order
    context_object_name = 'order'
    # form_type = OrderStatusForm
    form_class = OrderStatusForm
    pk_sing = 'pk'
    update = OrderLogic.update_instance

    def get_queryset(self):
        return Order.objects.select_related('customer', 'delivery__address').get(pk=self.pk_url_kwarg)

    def get_context_data(self, **kwargs):
        context = super(OrderFormView, self).get_context_data(**kwargs)
        context['purchase_items'] = serialize_list(self, get_purchase_item_model,
                                                   list(self.object.items.select_related('product_item__product')))

        context['order_statuses'] = serialize_list(self, get_key_name_model, MAGMAG_ORDER_STATUSES)
        return context

    def post(self, request, *args, **kwargs):
        return self.edit_handler(request, *args, **kwargs)


class ClientRequestListView(ListMixedView, SingleEditorMixin):
    template_name = 'dashboard/order/client_requests.html'
    model = ClientRequest
    context_object_name = 'client_request'
    converter = get_client_request_model
    paginate_by = 20
    form_type = ClientRequestFullForm
    update = MessageLogic.update_instance


    def get_queryset(self):
        return ClientRequest.objects.all().order_by('-date')

    def get_context_data(self, **kwargs):
        ctx = super(ListMixedView, self).get_context_data(**kwargs)
        ctx['page_size'] = self.paginate_by
        return ctx

    def post(self, request, *args, **kwargs):
        return self.edit_handler(request, *args, **kwargs)


class CallRequestListView(ListMixedView, SingleEditorMixin):
    template_name = 'dashboard/order/call_requests.html'
    model = CallRequest
    context_object_name = 'call_request'
    converter = get_call_request_model
    paginate_by = 20
    form_type = CallRequestFullForm
    update = MessageLogic.update_instance

    def get_queryset(self):
        return CallRequest.objects.all().order_by('-date')

    def get_context_data(self, **kwargs):
        ctx = super(ListMixedView, self).get_context_data(**kwargs)
        ctx['page_size'] = self.paginate_by
        return ctx

    def post(self, request, *args, **kwargs):
        return self.edit_handler(request, *args, **kwargs)