# -*- coding: utf-8 -*-
__author__ = 'dimitriy'
from django.conf.urls import patterns, url
from magmag_core.core.application import Application
from magmag_core.apps.pages.views import ContentView


class PagesApplication(Application):
    name = 'page'

    content_view = ContentView

    def get_urls(self):
        urlpatterns = patterns('',
            url(r'^(?P<slug>.*)$', self.content_view.as_view(), name='current'),
        )
        return self.post_process_urls(urlpatterns)


application = PagesApplication()