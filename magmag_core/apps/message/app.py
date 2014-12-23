# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

from django.conf.urls import patterns, url
from magmag_core.core.application import Application
from magmag_core.apps.message.views import ClientRequestView, CallRequestView


class MessageApplication(Application):
    name = 'message'
    client_request_view = ClientRequestView
    call_request_view = CallRequestView

    def get_urls(self):
        urlpatterns = patterns('',
                               url(r'^client_request$', self.client_request_view.as_view(), name='client_request'),
                               url(r'^call_request$', self.call_request_view.as_view(), name='call_request'),
                               )
        return self.post_process_urls(urlpatterns)


application = MessageApplication()