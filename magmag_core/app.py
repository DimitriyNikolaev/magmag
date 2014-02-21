# -*- coding: utf-8 -*-
__author__ = 'dimitriy'
from django.conf.urls import patterns, include
from magmag_core.core.application import Application


from magmag_core.apps.dashboard.app import application as dashboard_app
from magmag_core.apps.catalogue.app import  application as catalogue_app


class Magmag(Application):
    name = 'magmag'

    dashboard_app = dashboard_app
    catalogue_app = catalogue_app

    def get_urls(self):
        urlpatterns = patterns('',
                               (r'^dashboard/', include(self.dashboard_app.urls)),
                               (r'^catalogue/', include(self.catalogue_app.urls))
                               )
        return urlpatterns

application = Magmag()