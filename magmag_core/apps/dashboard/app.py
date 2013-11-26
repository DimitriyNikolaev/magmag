# -*- coding: utf-8 -*-
__author__ = 'dimitriy'
from django.conf.urls import patterns, url, include
from django.contrib.admin.views.decorators import staff_member_required
from magmag_core.apps.dashboard.views import IndexView
from magmag_core.apps.dashboard.catalogue.app import application as catalogue_app

from magmag_core.core.application import Application


class DashboardApplication(Application):
    name = 'dashboard'

    index_view = IndexView
    catalogue_application = catalogue_app

    def get_urls(self):
        urlpatterns = patterns('',
            url(r'^$', self.index_view.as_view(), name='dashboard-index'),
            url(r'^catalogue/', include(self.catalogue_application.urls))
        )
        return self.post_process_urls(urlpatterns)

    def get_url_decorator(self, url_name):
        return staff_member_required


application = DashboardApplication()