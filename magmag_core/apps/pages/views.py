# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

from django.views.generic import DetailView
from magmag_core.apps.pages.models import Page


class ContentView(DetailView):
    template_name = 'pages/page_template.html'
    model = Page
    context_object_name = 'page'
