__author__ = 'dimitriy'

from django.db import models
from django.utils.translation import ugettext_lazy as _
from magmag_core.apps.account.models import *


class AbstractProfile(models.Model):
    email = models.EmailField(_("Email"), blank=False, null=False, unique=True)
    phone = models.CharField(_("Phone"), max_length=18, blank=True, null=True)
    total_sum = models.DecimalField(_("Total_Sum"), blank=True, null=True, max_digits=8, decimal_places=2)
    name = models.CharField(_("Name"), blank=False, null=False, default='fio', max_length=80)
    is_subscribe = models.BooleanField(_("Is_subscribe"), default=True, blank=False, null=False)

    class Meta:
        abstract = True
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")


class AbstractAddress(models.Model):
    postal_code = models.CharField(_("Postal_Code"), max_length=6, blank=True, null=True)
    address = models.CharField(_("Address"), max_length=320, blank=True, null=True)
    name = models.CharField(_("Name"), blank=False, null=False, default='fio', max_length=80)
    profile = models.ForeignKey('Profile', related_name='addresses', verbose_name=_("Addresses"))

    class Meta:
        abstract = True
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")