# -*- coding: utf-8 -*-
__author__ = 'dimitriy'
from django.conf.urls import patterns, include
from magmag_core.core.application import Application


from magmag_core.apps.dashboard.app import application as dashboard_app


class Magmag(Application):
    name = 'magmag'

    dashboard_app = dashboard_app

    def get_urls(self):
        urlpatterns = patterns('', (r'^dashboard/', include(self.dashboard_app.urls)))
        return urlpatterns

application = Magmag()