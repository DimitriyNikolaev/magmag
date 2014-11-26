# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractMessage(models.Model):
    date = models.DateTimeField(_('Date'), null=False, blank=False, auto_now_add=True)
    viewed = models.BooleanField(_('Viewed'), null=False, blank=False, default=False)

    class Meta:
        abstract = True


class AbstractEmailMessage(AbstractMessage):
    message = models.TextField(_('Message'), null=False, blank=False)
    email = models.EmailField(_('Email'), null=False, blank=False)

    class Meta:
        abstract = True


class AbstractCallRequest(AbstractMessage):
    phone = models.CharField(_('Phone'), null=False, blank=False, max_length=16)

    class Meta:
        abstract = True