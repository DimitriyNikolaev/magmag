__author__ = 'dimitriy'

from django.conf.urls import patterns, url
from magmag_core.core.application import Application
from magmag_core.apps.order.views import CheckoutView


class OrderApplication(Application):
    name = 'order'

    checkout_view = CheckoutView

    def get_urls(self):
        urlpatterns = patterns('',
            url(r'^$', self.checkout_view.as_view(), name='checkout')
        )
        return self.post_process_urls(urlpatterns)


application = OrderApplication()