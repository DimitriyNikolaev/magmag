__author__ = 'dimitriy'

from django.conf.urls import patterns, url
from magmag_core.core.application import Application
from magmag_core.apps.order.views import CheckoutView, ThankYouView


class OrderApplication(Application):
    name = 'order'

    checkout_view = CheckoutView
    thank_you_view = ThankYouView

    def get_urls(self):
        urlpatterns = patterns('',
            url(r'^$', self.checkout_view.as_view(), name='checkout'),
            url(r'^thankyou/(?P<slug>.*)$', self.thank_you_view.as_view(), name='thank_you')
        )
        return self.post_process_urls(urlpatterns)


application = OrderApplication()