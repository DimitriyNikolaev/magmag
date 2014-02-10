# -*- coding: utf-8 -*-
__author__ = 'dimitriy'
from django.contrib.admin.views.decorators import staff_member_required
from django.conf.urls import patterns, url
from magmag_core.core.application import Application
from magmag_core.apps.dashboard.nav import Node, register
from magmag_core.apps.dashboard.catalogue.views import ProductListView, CategoryListView, StoreListView, ProductFormView, \
    ProductItemsView, ProductImagesView
from django.utils.translation import ugettext_lazy as _


node = Node(_('Catalogue'))
node.add_child(Node(_('Products'), 'magmag:dashboard:products', url_kwargs={'content_type': 'template'}))
node.add_child(Node(_('Categories'), 'magmag:dashboard:categories', url_kwargs={'content_type': 'template'}))
node.add_child(Node(_('Stores'), 'magmag:dashboard:stores', url_kwargs={'content_type': 'template'}))
register(node, 10)


class CatalogueApplication(Application):
    name = None
    products = ProductListView
    categories = CategoryListView
    stores = StoreListView
    product = ProductFormView
    product_items = ProductItemsView
    product_images = ProductImagesView

    def get_urls(self):
        urlpatterns = patterns('',
                               url(r'^products/(?P<content_type>[-\w]+)$', self.products.as_view(),
                                   name='products'),
                               url(r'^categories/(?P<content_type>[-\w]+)$', self.categories.as_view(),
                                   name='categories'),
                               url(r'^stores/(?P<content_type>[-\w]+)$', self.stores.as_view(),
                                   name='stores'),
                               url(r'^product/(?P<pk>\d+)/(?P<content_type>[-\w]+)$', self.product.as_view(),
                                   name='product'),
                               url(r'^productitems/(?P<pk>\d+)/(?P<content_type>[-\w]+)$', self.product_items.as_view(),
                                   name='product_items'),
                               url(r'^productimages/(?P<pk>\d+)/(?P<content_type>[-\w]+)$', self.product_images.as_view(),
                                   name='product_images')
                               )

        return self.post_process_urls(urlpatterns)

    def get_url_decorator(self, url_name):
        return staff_member_required


application = CatalogueApplication()