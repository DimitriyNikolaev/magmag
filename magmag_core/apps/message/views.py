# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

import json
from django.http.response import HttpResponse
from django.views.generic import FormView
from django.utils.translation import ugettext_lazy as _
from magmag_core.apps.message.forms import ClientRequestForm, CallRequestForm


class ClientRequestView(FormView):
    form_class = ClientRequestForm
    success_msg = _('Thanks for your request')

    def form_valid(self, form):
        message = form.save()
        res = {'success': True, 'msg': unicode(self.success_msg)}
        return HttpResponse(json.dumps(res, ensure_ascii=False), content_type="application/json")

    def form_invalid(self, form):
        res = {'success': False, 'msg': next(iter(form.errors.values()))[0]}
        return HttpResponse(json.dumps(res, ensure_ascii=False), content_type="application/json")


class CallRequestView(FormView):
    form_class = CallRequestForm
    success_msg = _('Thanks for your request')

    def form_valid(self, form):
        message = form.save()
        res = {'success': True, 'msg': unicode(self.success_msg)}
        return HttpResponse(json.dumps(res, ensure_ascii=False), content_type="application/json")

    def form_invalid(self, form):
        res = {'success': False, 'msg': next(iter(form.errors.values()))[0]}
        return HttpResponse(json.dumps(res, ensure_ascii=False), content_type="application/json")
