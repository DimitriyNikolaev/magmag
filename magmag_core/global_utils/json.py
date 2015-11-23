__author__ = 'dimitriy'

#import json
import simplejson as json


def serialize_list(obj, converter, instance):
    source = [converter(obj, n) for n in instance]
    data = json.dumps(source, ensure_ascii=False)
    return u"{'data': %s, 'total': %d}" % (data, len(source),)


def deserialize_list(str):
    return json.loads(str)