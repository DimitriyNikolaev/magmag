__author__ = 'dimitriy'

from django.views.generic import TemplateView, ListView, DetailView
from magmag_core.apps.catalogue.models_logic import CategoryLogic
from magmag_core.apps.catalogue.models import Product
from django.utils.translation import ugettext_lazy as _


class IndexView(ListView):
    template_name = 'catalogue/index.html'
    model = Product
    context_object_name = "products"
    paginate_by = 16

    def get_queryset(self):
        return Product.objects.filter(hidden=False, price__gt=0)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        res = []
        for item in CategoryLogic.get_category_nav(None):
            res.append(item)
        context['categories'] = res
        return context


class CategoryView(ListView):
    template_name = 'catalogue/index.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 16

    def get_queryset(self):
        pk = self.kwargs.get('pk', None)
        slug = self.kwargs.get('slug', None)
        if pk is not None:
            return Product.objects.filter(categories__pk=pk, hidden=False, price__gt=0)
        elif slug is not None:
            return Product.objects.filter(categories__slug=slug, hidden=False, price__gt=0)
        else:
            raise AttributeError(_("Category identifier is None"))

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        res = []
        for item in CategoryLogic.get_category_nav(None):
            res.append(item)
        context['categories'] = res
        return context


class ProductView(DetailView):
    template_name = 'catalogue/product.html'
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        return context