__author__ = 'dimitriy'

import json


def serialize_list(obj, converter, instance):
    source = [converter(obj, n) for n in instance]
    data = json.dumps(source, ensure_ascii=False)
    return u"{'data': %s, 'total': %d}" % (data, len(source),)
