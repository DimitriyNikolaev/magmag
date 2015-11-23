# -*- coding: utf-8 -*-
__author__ = 'dimitriy'


from magmag_core.apps.base_models.models_logic_base import BaseLogic


class PageLogic(BaseLogic):
    pass


class PageImageLogic(BaseLogic):
    @staticmethod
    def update_instance(view, forma):
        if not forma.is_valid():
            return False, None
        try:
            old_id = forma.data['id']
            instance = forma.save()
            return True, {'id': instance.id,
                          'page_id': instance.page.id,
                          'url': instance.image.url if instance.image else '/static/magmag_core/img/add_large.png',
                          'caption': instance.caption,
                          'deleted': False,
                          'old_id': old_id}
        except Exception as x:
            return False, None