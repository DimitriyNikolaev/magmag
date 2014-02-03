# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

from django.http import HttpResponse
from django.views.generic import TemplateView, UpdateView
from magmag_core.view.base_views import SingleEditMixedView, ListMixedView, SingleTreeEditorMixin, SingleEditorMixin
from magmag_core.apps.catalogue.models import Category, Store, Product, ProductItem
from magmag_core.apps.dashboard.catalogue.view_models import get_category_tree_model, get_store_model, \
    get_product_grid_model, get_product_item_model
from magmag_core.apps.catalogue.models_logic import CategoryLogic, StoreLogic, ProductLogic
from magmag_core.apps.dashboard.catalogue.forms import CategoryForm, StoreForm, ProductForm


class ProductListView(ListMixedView, SingleEditorMixin):
    template_name = 'dashboard/catalogue/products.html'
    model = Product
    context_object_name = 'products'
    converter = get_product_grid_model
    delete = ProductLogic.delete_instance
    paginate_by = 20

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super(ListMixedView, self).get_context_data(**kwargs)
        ctx['page_size'] = self.paginate_by
        return ctx

    def post(self, request, *args, **kwargs):
        return self.edit_handler(request, *args, **kwargs)


class CategoryListView(ListMixedView, SingleTreeEditorMixin):
    template_name = 'dashboard/catalogue/categories.html'
    model = Category
    context_object_name = 'categories'
    converter = get_category_tree_model
    delete = CategoryLogic.delete_instance
    update = CategoryLogic.update_instance
    move = CategoryLogic.move_category
    form_type = CategoryForm

    #def get_context_data(self, **kwargs):
    #    ctx = super(CategoryListView, self).get_context_data(**kwargs)
    #    return ctx

    def get_queryset(self):
        return list(Category.tree.root_nodes())

    def post(self, request, *args, **kwargs):
        return self.edit_handler(request, *args, **kwargs)


class StoreListView(ListMixedView, SingleEditorMixin):
    template_name = 'dashboard/catalogue/stores.html'
    model = Store
    context_object_name = 'stores'
    converter = get_store_model
    delete = StoreLogic.delete_instance
    update = StoreLogic.update_instance
    form_type = StoreForm

    def get_queryset(self):
        return Store.objects.all()

    def post(self, request, *args, **kwargs):
        return self.edit_handler(request, *args, **kwargs)


class ProductFormView(SingleEditMixedView, SingleEditorMixin):
    template_name = 'dashboard/catalogue/product_form.html'
    model = Product
    context_object_name = 'product'
    form_type = ProductForm
    pk_sing = 'pk'
    update = ProductLogic.update_instance

    def post(self, request, *args, **kwargs):
        return self.edit_handler(request, *args, **kwargs)


class ProductItemsView(ListMixedView):
    context_object_name = 'product_items'
    model = ProductItem
    converter = get_product_item_model
    paginate_by = 7

    def get_queryset(self):
        pk = self.kwargs.get('pk', None)
        return list(ProductItem.objects.filter(product=pk).prefetch_related('stock_items__store'))