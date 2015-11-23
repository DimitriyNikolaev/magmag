# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

from magmag_core.view.base_views import SingleEditMixedView, ListMixedView, SingleTreeEditorMixin, SingleEditorMixin, \
    FormsetEditorMixin
from magmag_core.apps.pages.models import Page, PageImage
from magmag_core.apps.dashboard.dashboard_pages.view_models import get_page_model, get_page_image_model
from magmag_core.apps.dashboard.dashboard_pages.forms import PageForm, PageImageForm
from magmag_core.apps.pages.models_logic import PageLogic, PageImageLogic


class PageListView(ListMixedView, SingleEditorMixin):
    template_name = 'dashboard/pages/pages.html'
    model = Page
    context_object_name = 'pages'
    converter = get_page_model
    paginate_by = 20

    def get_queryset(self):
        return Page.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super(ListMixedView, self).get_context_data(**kwargs)
        ctx['page_size'] = self.paginate_by
        return ctx


class PageFormView(SingleEditMixedView, SingleEditorMixin):
    template_name = 'dashboard/pages/page_form.html'
    model = Page
    context_object_name = 'page'
    # form_type = PageForm
    form_class = PageForm
    pk_sing = 'pk'
    update = PageLogic.update_instance

    def get_context_data(self, **kwargs):
        context = super(PageFormView, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        return self.edit_handler(request, *args, **kwargs)


class PageImageListView(ListMixedView, SingleEditorMixin):

    model = PageImage
    context_object_name = 'image'
    converter = get_page_image_model
    form_type = PageImageForm
    update = PageImageLogic.update_instance
    delete = PageImageLogic.delete_instance

    def get_queryset(self):
        pk = self.kwargs.get('page', None)
        res = list(PageImage.objects.filter(page=pk))
        res.append(PageImage(id=0, caption='', page=Page(id=pk)))
        return res

    def post(self, request, *args, **kwargs):
        return self.edit_handler(request, *args, **kwargs)