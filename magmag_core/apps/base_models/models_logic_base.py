# -*- coding: utf-8 -*-
__author__ = 'dimitriy'


class BaseLogic(object):
    @staticmethod
    def update_instance(view, forma):
        if len(forma.errors) > 0 and not forma.is_valid():
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
