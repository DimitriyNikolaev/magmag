# -*- coding: utf-8 -*-
__author__ = 'dimitriy'


def get_key_name_model(view, item):
    return {
        'key': item[0],
        'name': unicode(item[1]),# str(item[1]),
    }