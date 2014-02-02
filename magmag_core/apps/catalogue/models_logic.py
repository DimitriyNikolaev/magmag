# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

from magmag_core.apps.catalogue.models import Category, Store


class BaseLogic(object):
    @staticmethod
    def update_instance(view, forma):
        if len(forma.errors) > 0 and forma.is_valid():
            return False
        try:
            instance = forma.save()
            return True
        except Exception as x:
            return False

    @staticmethod
    def delete_instance(view, src_id):
        if view.model is not None:
            src_node = view.model.objects.get(pk=src_id)
            if src_node:
                try:
                    src_node.delete()
                    return True
                except Exception as x:
                    return False
        else:
            return False

    class Meta:
        abstract = True


class ProductLogic(BaseLogic):
    @staticmethod
    def update_instance(view, forma):
        if len(forma.errors) > 0 and forma.is_valid():
            return False
        try:
            instance = forma.save()
            return True
        except Exception as x:
            return False


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
                return True
            except Exception as x:
                return False

    @staticmethod
    def delete_instance(view, src_id):
        src_node = Category.tree.get(pk=src_id)
        if src_node:
            try:
                src_node.delete()
                return True
            except Exception as x:
                return False


class StoreLogic(BaseLogic):
    pass