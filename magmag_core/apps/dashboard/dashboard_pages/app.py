# -*- coding: utf-8 -*-
__author__ = 'dimitriy'


from django.contrib.admin.views.decorators import staff_member_required
from django.conf.urls import patterns, url
from magmag_core.core.application import Application
from magmag_core.apps.dashboard.nav import Node, register
from django.utils.translation import ugettext_lazy as _
from magmag_core.apps.dashboard.dashboard_pages.views import PageListView, PageFormView, PageImageListView



node = Node(_('Content'))
node.add_child(Node(_('Pages'), 'magmag:dashboard:pages', url_kwargs={'content_type': 'template'}))
#node.add_child(Node(_('Categories'), 'magmag:dashboard:categories', url_kwargs={'content_type': 'template'}))
# node.add_child(Node(_('Stores'), 'magmag:dashboard:stores', url_kwargs={'content_type': 'template'}))
register(node, 30)


class PageApplication(Application):
    name = None
    pages = PageListView
    page = PageFormView
    page_images = PageImageListView

    def get_urls(self):
        urlpatterns = patterns('',
                               url(r'^pages/(?P<content_type>[-\w]+)$', self.pages.as_view(),
                                   name='pages'),
                               url(r'^page/(?P<pk>\d+)/(?P<content_type>[-\w]+)$', self.page.as_view(),
                                   name='page'),
                               url(r'^page/(?P<page>\d+)/images/(?P<content_type>[-\w]+)$', self.page_images.as_view(),
                                   name='page_images'),
                               )

        return self.post_process_urls(urlpatterns)

    def get_url_decorator(self, url_name):
        return staff_member_required


application = PageApplication()