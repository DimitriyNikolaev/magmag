__author__ = 'dimitriy'
from django.conf.urls import patterns, url
from magmag_core.apps.catalogue.views import IndexView, CategoryView


from magmag_core.core.application import Application


class CatalogueApplication(Application):
    name = 'catalogue'

    index_view = IndexView
    category_view = CategoryView

    def get_urls(self):
        urlpatterns = patterns('',
            url(r'^$', self.index_view.as_view(), name='catalogue-index'),
            url(r'^category/(?P<pk>\d+)/$', self.category_view.as_view(), name='catalogue-category'),
            url(r'^category/(?P<slug>[-\w]+)/$', self.category_view.as_view(), name='slug-catalogue-category'),
        )
        return self.post_process_urls(urlpatterns)


application = CatalogueApplication()