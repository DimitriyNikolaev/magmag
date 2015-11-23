# -*- coding: utf-8 -*-
__author__ = 'dimitriy'
from django.conf.urls import patterns, include
from magmag_core.core.application import Application


from magmag_core.apps.dashboard.app import application as dashboard_app
from magmag_core.apps.catalogue.app import  application as catalogue_app
from magmag_core.apps.order.app import application as order_app
from magmag_core.apps.pages.app import application as pages_app
from magmag_core.apps.message.app import  application as message_app
from magmag_core.apps.promo.app import  application as promo_app


class Magmag(Application):
    name = 'magmag'

    dashboard_app = dashboard_app
    catalogue_app = catalogue_app
    order_app = order_app
    pages_app = pages_app
    message_app = message_app
    promo_app = promo_app

    def get_urls(self):
        urlpatterns = patterns('',
                               (r'^$', include(self.promo_app.urls)),
                               (r'^dashboard/', include(self.dashboard_app.urls)),
                               (r'^catalogue/', include(self.catalogue_app.urls)),
                               (r'^checkout/', include(self.order_app.urls)),
                               (r'^content/', include(self.pages_app.urls)),
                               (r'^message/', include(self.message_app.urls))
                               )
        return urlpatterns

application = Magmag()