# -*- coding: utf-8 -*-
__author__ = 'dimitriy'


def upload_to_image_page_path(instance, filename):
    return 'pages/%s/%s' % (instance.page.id, filename,)