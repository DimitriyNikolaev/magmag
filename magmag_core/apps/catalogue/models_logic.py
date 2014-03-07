# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

import json
from magmag_core.apps.catalogue.models import Category, Store, ProductItem, StockItem



class BaseLogic(object):
    @staticmethod
    def update_instance(view, forma):
        if len(forma.errors) > 0 and forma.is_valid():
            return False, None
        try:
            instance = forma.save()
            return True, None
        except Exception as x:
            return False, None

    @staticmethod
    def delete_instance(view, src_id):
        if view.model is not None:
            src_node = view.model.objects.get(pk=src_id)
            if src_node:
                try:
                    src_node.delete()
                    return True, None
                except Exception as x:
                    return False, None
        else:
            return False, None

    class Meta:
        abstract = True


class ProductLogic(BaseLogic):
    @staticmethod
    def update_instance(view, forma):
        if not forma.is_valid():
            return False, None
        try:
            items = json.loads(forma.data['product_items'])
            category = Category.objects.get(pk=forma.data['category'])
            instance = forma.save()
            ProductLogic.add_to_single_category(instance, category)
            for item in items:
                p_item = ProductItem(
                    pk=item['id'] if item['id'] > 0 else None,
                    color=item['color'],
                    size=item['size']
                )
                instance.items.add(p_item)
                for rest in item['rests']:
                    p_rest = StockItem(
                        pk=rest['id'] if rest['id'] > 0 else None,
                        count=rest['count'])
                    p_rest.store = Store(rest['store_id'])
                    p_item.stock_items.add(p_rest)
            return True, {'id': instance.id}
        except Exception as x:
            return False, None
    @staticmethod
    def add_to_single_category(instance, category):
        if category:
            categories = instance.categories.all()
            for cat in categories:
                cat.products.remove(instance)
            category.products.add(instance)


class CategoryLogic(BaseLogic):
    @staticmethod
    def move_category(view, src_id, target_id):
        src_node = Category.tree.get(pk=src_id)
        target_node = None
        if target_id != 'root':
            target_node = Category.tree.get(pk=target_id)
        if src_node:
            try:
                src_node.move_to(target_node, 'last-child')
                return True, None
            except Exception as x:
                return False, None

    @staticmethod
    def delete_instance(view, src_id):
        src_node = Category.tree.get(pk=src_id)
        if src_node:
            try:
                src_node.delete()
                return True, None
            except Exception as x:
                return False, None

    @staticmethod
    def get_category_nav(categories=None):
        root = False
        if categories is None:
            root = True
            #get the root categories
            categories = Category.objects.filter(parent=None)
            categories[0].active = True
        else:
            yield 'in'

        for category in categories:
            yield category
            subcats = Category.objects.select_related().filter(parent=category)
            if len(subcats):
                category.leaf = False
                for x in CategoryLogic.get_category_nav(subcats):
                    yield x
            else:
                category.leaf=True
        yield '' if root else 'out'


class StoreLogic(BaseLogic):
    pass