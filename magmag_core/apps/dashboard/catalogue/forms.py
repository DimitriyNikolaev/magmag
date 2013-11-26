# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

from django.forms import ModelForm
from magmag_core.apps.catalogue.models import Category, Store


class CategoryForm(ModelForm):
    class Meta:
        model = Category


class StoreForm(ModelForm):
    class Meta:
        model = Store