# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

from django.http import HttpResponse
from django.views.generic import View
from magmag_core.view.base_views import SingleEditMixedView, ListMixedView, SingleTreeEditorMixin, SingleEditorMixin, \
    FormsetEditorMixin
from magmag_core.apps.catalogue.models import Category, Store, Product, ProductItem, ProductImage
from magmag_core.apps.dashboard.dashboard_catalogue.view_models import get_category_tree_model, get_store_model, \
    get_product_grid_model, get_product_item_model, get_product_image_model
from magmag_core.apps.catalogue.models_logic import CategoryLogic, StoreLogic, ProductLogic
from magmag_core.apps.dashboard.dashboard_catalogue.forms import CategoryForm, StoreForm, ProductForm, ProductImageFormSet
from magmag_core.global_utils.json import serialize_list


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
    # form_type = ProductForm
    form_class = ProductForm
    pk_sing = 'pk'
    update = ProductLogic.update_instance

    def get_context_data(self, **kwargs):
        context = super(ProductFormView, self).get_context_data(**kwargs)
        context['stores'] = serialize_list(self, get_store_model, list(Store.objects.all()))
        context['product_items'] = serialize_list(self, get_product_item_model,
                                                  list(ProductItem.objects.
                                                       filter(product=self.object.pk).
                                                       prefetch_related('stock_items__store')))

        res = list(ProductImage.objects.filter(product=self.object.pk))
        for idx, val in enumerate(res):
            val.display_order = idx
        res.append(ProductImage(id=0, caption='', display_order=len(res)))
        context['product_images'] = serialize_list(self, get_product_image_model, res)
        return context

    def post(self, request, *args, **kwargs):
        return self.edit_handler(request, *args, **kwargs)


class ProductItemsView(ListMixedView):
    context_object_name = 'product_items'
    model = ProductItem
    converter = get_product_item_model
    #paginate_by = 7

    def get_queryset(self):
        pk = self.kwargs.get('pk', None)
        return list(ProductItem.objects.filter(product=pk).prefetch_related('stock_items__store'))


class ProductImagesView(FormsetEditorMixin, View):
    base_model = Product
    image_formset = ProductImageFormSet

    def __init__(self, *args, **kwargs):
        self.formsets = {'image_formset': self.image_formset}

    def post(self, request, *args, **kwargs):
        return HttpResponse(self.edit_handler(request, *args, **kwargs), content_type="application/json")