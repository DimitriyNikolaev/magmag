# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from magmag_core.apps.pages.utils import upload_to_image_page_path


class Page(models.Model):
    title = models.CharField(_('Title'), max_length=255, null=False, blank=False, default=_('Title'))
    url = models.CharField(_('URL'), max_length=255, null=False, blank=False, default='/')
    display_name = models.CharField(_('Display name'), max_length=128, null=False, blank=False, default='page')
    content = models.TextField(_('Content'), null=False, blank=True)
    deletable = models.BooleanField(_('Deletable'), default=True)
    slug = models.SlugField(_('Slug'), max_length=255, db_index=True, editable=True, null=True, blank=True)

    @property
    def identifier(self):
        return self.id if self.id is not None else 0

    @property
    def safe_content(self):
        if self.content is not None:
            return self.content.replace('\n', "'\n+'")
        return ''

    def __unicode__(self):
        return self.display_name

    def __str__(self):
        return self.display_name


class PageImage(models.Model):
    page = models.ForeignKey(Page, related_name='images', verbose_name=_("Page"))
    image = models.ImageField(_("Image"), upload_to=upload_to_image_page_path)
    caption = models.CharField(_("Caption"), max_length=200, blank=True, null=True)