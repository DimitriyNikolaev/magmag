# -*- coding: utf-8 -*-
__author__ = 'dimitriy'
from django.conf.urls import patterns, url, include
from django.contrib.admin.views.decorators import staff_member_required
from magmag_core.apps.dashboard.views import IndexView
from magmag_core.apps.dashboard.dashboard_catalogue.app import application as catalogue_app
from magmag_core.apps.dashboard.dashboard_order.app import application as crm_app
from magmag_core.apps.dashboard.dashboard_pages.app import application as pages_app

from magmag_core.core.application import Application


class DashboardApplication(Application):
    name = 'dashboard'

    index_view = IndexView
    catalogue_application = catalogue_app
    crm_application = crm_app
    pages_application = pages_app

    def get_urls(self):
        urlpatterns = patterns('',
            url(r'^$', self.index_view.as_view(), name='dashboard-index'),
            url(r'^catalogue/', include(self.catalogue_application.urls)),
            url(r'^crm/', include(self.crm_application.urls)),
            url(r'^pages/', include(self.pages_application.urls)),
        )
        return self.post_process_urls(urlpatterns)

    def get_url_decorator(self, url_name):
        return staff_member_required


application = DashboardApplication()