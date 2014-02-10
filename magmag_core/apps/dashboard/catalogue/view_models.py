# -*- coding: utf-8 -*-
__author__ = 'dimitriy'


def get_category_tree_model(view, cat):
    res = {'id': cat.id,
           'name': cat.name,
           'description': cat.description,
           'slug': cat.slug,
           'image': cat.image.url if cat.image else None,
           'data': [get_category_tree_model(view, c) for c in cat.get_children()],
           'leaf': cat.is_leaf_node(),
           'expanded': True
           }
    return res


def get_store_model(view, store):
    return {
        'id': store.id,
        'name': store.name,
        'phone': store.phone,
        'address': store.address
    }


def get_product_grid_model(view, product):
    return {
        'id': product.id,
        'name': product.name,
        'image': product.image.url if product.image else '',
        'slug': product.slug,
        'date_added': product.date_added.strftime("%d.%m.%Y"),
        'article': product.article
    }


def get_product_item_model(view, product_item):
    return {
        'id': product_item.id,
        'color': product_item.color,
        'size': product_item.size,
        'rests': [
            {'id': rest.id,
             'item_id':  product_item.id,
             'store_id': rest.store.id,
             'store_name': rest.store.name,
             'count': rest.count}
            for rest in product_item.stock_items.all()]
    }


def get_product_image_model(view, product_image):
    return {
        'id': product_image.id,
        'src': product_image.original.url if product_image.original else '/static/magmag_core/img/add_large.png',
        'caption': product_image.caption,
        'order': product_image.display_order,
        'deleted': False
    }
