__author__ = 'dimitriy'
from django.conf.urls import patterns, url
from magmag_core.apps.catalogue.views import IndexView


from magmag_core.core.application import Application


class CatalogueApplication(Application):
    name = 'catalogue'

    index_view = IndexView

    def get_urls(self):
        urlpatterns = patterns('',
            url(r'^$', self.index_view.as_view(), name='catalogue-index')
        )
        return self.post_process_urls(urlpatterns)


application = CatalogueApplication()