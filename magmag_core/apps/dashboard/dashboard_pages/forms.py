# -*- coding: utf-8 -*-
__author__ = 'dimitriy'


from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from magmag_core.apps.pages.models import Page, PageImage


class PageForm(ModelForm):
    class Meta:
        model = Page


class PageImageForm(ModelForm):
    class Meta:
        model = PageImage


BasePageImageFormSet = inlineformset_factory(
    Page, PageImage, form=PageImageForm)


class PageImageFormSet(BasePageImageFormSet):
    def __init__(self, page_class, user, *args, **kwargs):
        super(PageImageFormSet, self).__init__(*args, **kwargs)