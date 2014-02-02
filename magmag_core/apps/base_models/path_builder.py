# -*- coding: utf-8 -*-
__author__ = 'dimitriy'


def upload_to_product_path(instance, filename):
    return 'products/%s/%s' % (instance.slug, filename,)


def upload_to_image_product_path(instance, filename):
    return 'products/%s/%s' % (instance.product.slug, filename,)