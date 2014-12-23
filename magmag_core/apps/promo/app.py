# -*- coding: utf-8 -*-
__author__ = 'dimitriy'


from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from magmag_core.core.application import Application


class PromoApplication(Application):
    name = 'promo'

    def get_urls(self):
        urlpatterns = patterns('',
            url(r'^$', RedirectView.as_view(url=reverse_lazy('magmag:catalogue:catalogue-index')), name='promo'),
        )
        return self.post_process_urls(urlpatterns)


application = PromoApplication()