# -*- coding: utf-8 -*-
__author__ = 'dimitriy'


def get_page_model(view, page):
    return {
        'id': page.id,
        'display_name': page.display_name,
        'title': page.title,
        'deletable': page.deletable,
        'url': page.url,
        'slug': page.slug
    }


def get_page_image_model(view, image):
    return {
        'id': image.id,
        'page_id': image.page.id,
        'url': image.image.url if image.image else '/static/magmag_core/img/add_large.png',
        'caption': image.caption,
        'deleted': False
    }
