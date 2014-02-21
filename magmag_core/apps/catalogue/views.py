__author__ = 'dimitriy'

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'catalogue/index.html'
    pass
