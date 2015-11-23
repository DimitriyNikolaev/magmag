# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

from django.contrib.admin.views.decorators import staff_member_required
from django.conf.urls import patterns, url
from magmag_core.core.application import Application
from magmag_core.apps.dashboard.nav import Node, register
from django.utils.translation import ugettext_lazy as _
from magmag_core.apps.dashboard.dashboard_order.views import OrderListView, OrderFormView, ClientRequestListView, CallRequestListView



node = Node(_('CRM'))
node.add_child(Node(_('Orders'), 'magmag:dashboard:orders', url_kwargs={'content_type': 'template'}))
node.add_child(Node(_('Messages'), 'magmag:dashboard:client_requests', url_kwargs={'content_type': 'template'}))
node.add_child(Node(_('Calls'), 'magmag:dashboard:call_requests', url_kwargs={'content_type': 'template'}))
register(node, 20)


class OrderApplication(Application):
    name = None
    orders = OrderListView
    order = OrderFormView
    messages = ClientRequestListView
    calls = CallRequestListView

    def get_urls(self):
        urlpatterns = patterns('',
                               url(r'^orders/(?P<content_type>[-\w]+)$', self.orders.as_view(),
                                   name='orders'),
                               url(r'^order/(?P<pk>\d+)/(?P<content_type>[-\w]+)$', self.order.as_view(),
                                   name='order'),
                               url(r'^client_requests/(?P<content_type>[-\w]+)$', self.messages.as_view(),
                                   name='client_requests'),
                               url(r'^call_requests/(?P<content_type>[-\w]+)$', self.calls.as_view(),
                                   name='call_requests'),
                               )

        return self.post_process_urls(urlpatterns)

    def get_url_decorator(self, url_name):
        return staff_member_required


application = OrderApplication()