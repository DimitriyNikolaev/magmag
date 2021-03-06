# -*- coding: utf-8 -*-
__author__ = 'dimitriy'
import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from mptt.managers import TreeManager
from mptt.models import MPTTModel, TreeForeignKey
from magmag_core.apps.base_models.path_builder import upload_to_product_path, upload_to_image_product_path
from magmag_core.apps.catalogue.models import *
from magmag_core.global_utils.common import get_first


#Catalog----------------------------------------------------------------------------------------------------------------
class AbstractStore(models.Model):
    name = models.CharField(_('Name'), max_length=64, db_index=True, null=False, blank=False, editable=True)
    phone = models.CharField(_('Phone'), max_length=24)
    address = models.CharField(_('Address'), max_length=256)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name']
        verbose_name = _('Store')
        verbose_name_plural = _('Stores')


class AbstractCategory(MPTTModel):
    name = models.CharField(_('Name'), max_length=255, db_index=True)
    description = models.TextField(_('Description'), blank=True, null=True)
    image = models.ImageField(_('Image'), upload_to='categories', blank=True, null=True)
    slug = models.SlugField(_('Slug'), max_length=255, db_index=True, editable=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    tree = TreeManager()
    products = models.ManyToManyField('Product', blank=True, verbose_name=_("products"), related_name='categories')
    leaf = False

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        abstract = True
        ordering = ['name']
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    @property
    def get_class_name(self):
        return self.__class__.__name__


class AbstractProduct(models.Model):
    name = models.CharField(_('Name'), max_length=255, db_index=True)
    description = models.TextField(_('Description'), blank=True, null=True)
    image = models.ImageField(_('Image'), upload_to=upload_to_product_path, blank=True, null=True)
    slug = models.SlugField(_('Slug'), max_length=255, db_index=True, editable=True, unique=True)
    date_added = models.DateField(_('Date_Added'), editable=False, blank=False, null=False,
                                  default=now)
    article = models.CharField(_('Article'), max_length=10, db_index=True, blank=False, null=False, default='')
    price = models.DecimalField(_('Price'), blank=False, null=False, default=0, max_digits=8, decimal_places=2)
    hidden = models.BooleanField(_('Hidden'), blank=False, null=False, default=False)

    @property
    def category(self):
        if self.pk is None:
            return None
        return get_first(self.categories.all(), '')
    @property
    def descr(self):
        return self.description if self.description is not None else ''

    @property
    def identifier(self):
        return self.id if self.id is not None else 0

    @property
    def get_class_name(self):
        return self.__class__.__name__

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        unique_together = ('slug', 'article')
        ordering = ['name']
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class AbstractProductItem(models.Model):
    product = models.ForeignKey('Product', related_name='items', verbose_name=_("Product"))
    color = models.CharField(_('Color'), max_length=64, db_index=True)
    size = models.CharField(_('Size'), max_length=5, db_index=True)

    def __unicode__(self):
        return '%s - %s' % (self.color, self.size,)

    def __str__(self):
        return '%s - %s' % (self.color, self.size,)


    class Meta:
        abstract = True
        ordering = ['size']
        verbose_name = _('Item')
        verbose_name_plural = _('Items')


class AbstractStockItem(models.Model):
    product_item = models.ForeignKey('ProductItem', related_name='stock_items', verbose_name=_("ProductItem"))
    store = models.ForeignKey('Store', related_name='stock_items', verbose_name=_("Store"))
    count = models.PositiveIntegerField(_('Count'), default=0, null=False, blank=False, editable=True)

    class Meta:
        abstract = True
        unique_together = ('product_item', 'store')
        verbose_name = _('StockItem')
        verbose_name_plural = _('StockItems')



class AbstractProductImage(models.Model):
    """
    An image of a product
    """
    product = models.ForeignKey(
        'Product', related_name='images', verbose_name=_("Product"))
    original = models.ImageField(
        _("Original"), upload_to=upload_to_image_product_path)
    preview = models.ImageField(
        _("Preview"), upload_to=upload_to_image_product_path)
    thumbnail = models.ImageField(
        _("Thumbnail"), upload_to=upload_to_image_product_path)
    caption = models.CharField(
        _("Caption"), max_length=200, blank=True, null=True)

    # Use display_order to determine which is the "primary" image
    display_order = models.PositiveIntegerField(_("Display Order"), default=1,
        help_text=_("""An image with a display order of
                       1 will be the primary image for a product"""))
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)

    def __unicode__(self):
        return self.caption

    def __str__(self):
        return self.caption

    class Meta:
        abstract = True
        #unique_together = ("product", "display_order")
        ordering = ["display_order"]
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')
#-----------------------------------------------------------------------------------------------------------------------


#Account----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------