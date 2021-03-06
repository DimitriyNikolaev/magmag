__author__ = 'dimitriy'

from django.db.models import Prefetch
from django.views.generic import TemplateView, ListView, DetailView
from magmag_core.apps.catalogue.models_logic import CategoryLogic
from magmag_core.apps.catalogue.models import Product, ProductItem, StockItem
from django.utils.translation import ugettext_lazy as _


class IndexView(ListView):
    template_name = 'catalogue/index.html'
    model = Product
    context_object_name = "products"
    paginate_by = 6

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
    paginate_by = 6

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
        context['images'] = list(self.object.images.all())
        context['items'] = ProductItem.objects.prefetch_related(
            Prefetch('stock_items', queryset=StockItem.objects.select_related('store')),
            'stock_items__reservation'
        ).filter(product=self.object) # list(self.object.items.pre.all())
        context['sizes'] = dict((str(hash(s)).replace('-', '_'), s) for s in set([el.size for el in context['items']]))
        context['colors'] = dict((str(hash(c)).replace('-', '_'), c) for c in set([el.color for el in context['items']]))
        return context