# -*- coding: utf-8 -*-
__author__ = 'dimitriy'
from django.utils import encoding
import unidecode
try:
    # Django 1.5 have some permutations.
    from django.utils import text as src_pkg
    from django.utils.text import slugify as dj_slugify
except ImportError:
    from django.template import defaultfilters as src_pkg
    from django.template.defaultfilters import slugify as dj_slugify


def slugify(value):
    value = encoding.smart_unicode(value)
    return dj_slugify(encoding.smart_unicode(unidecode.unidecode(value)))