# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

import json
from django.http import HttpResponse
from django.views.generic import ListView
from django.http import Http404
from django.utils.translation import ugettext_lazy as _


class JsonResponseMixin(object):
    def render_to_response_json(self, context):
        return HttpResponse(self.convert_context_to_json(context), content_type='application/json')

    def convert_context_to_json(self, context, extract_from_queryset=None):
        pass


class ListMixedView(JsonResponseMixin, ListView):
    converter = None

    def get(self, request, *args, **kwargs):
        if kwargs['content_type'] == 'json' or self.template_name is None:
            self.object_list = self.get_queryset()
            allow_empty = self.get_allow_empty()

            if not allow_empty:
                # When pagination is enabled and object_list is a queryset,
                # it's better to do a cheap query than to load the unpaginated
                # queryset in memory.
                if (self.get_paginate_by(self.object_list) is not None
                    and hasattr(self.object_list, 'exists')):
                    is_empty = not self.object_list.exists()
                else:
                    is_empty = len(self.object_list) == 0
                if is_empty:
                    raise Http404(_("Empty list and '%(class_name)s.allow_empty' is False.")
                            % {'class_name': self.__class__.__name__})
            context = self.get_context_data(object_list=self.object_list)
            return JsonResponseMixin.render_to_response_json(self, context)
        else:
            return super(ListMixedView,self).get(self, request, *args, **kwargs)

    def convert_context_to_json(self, context, extract_from_queryset=None):
        source = [self.converter(n) for n in context[self.context_object_name]]
        data = json.dumps(source, ensure_ascii=False)
        return u"{'data': %s, 'total': %d}" % (data, context["paginator"].count if context['paginator'] is not None else len(source),)


class SingleEditorMixin(object):
    update = None
    delete = None
    pk_sing = 'id'
    form_type = None

    def get_object(self):
        pk = self.request.POST.get(self.pk_sing)
        if pk == '':
            return None
        return self.model.objects.get(pk=pk)

    def edit_handler(self, request, *arg, **kwargs):
        action = request.POST.get('action', '').lower()
        if action == 'delete':
            del_id = request.POST.get('delElId', 0).lower()
            if self.delete is not None:
                deleted = self.delete(del_id)
                return HttpResponse('success' if deleted else 'failure')
            else:
                return HttpResponse('success' if False else 'Undefined object form')
        elif action == 'update':
            form_kwargs = {'data': self.request.POST, 'files': self.request.FILES}
            form_kwargs.update({'instance': self.get_object()})
            if self.form_type is not None and self.update is not None:
                form = self.form_type(**form_kwargs)
                success = self.update(form)
                return HttpResponse(json.dumps({'success': success, 'msg': 'success'}),
                                    content_type='application/json')
            else:
                return HttpResponse(json.dumps({'success': False, 'msg': 'Undefined object form'}),
                                    content_type='application/json')


class SingleTreeEditorMixin(SingleEditorMixin):
    move = None

    def edit_handler(self, request, *arg, **kwargs):
        action = request.POST.get('action', '').lower()
        if action == 'move':
            src_id = request.POST.get('ddElId', 0).lower()
            target_id = request.POST.get('targetElId', 0).lower()
            if self.move is not None:
                moved = self.move(src_id, target_id)
                return HttpResponse('success' if moved else 'failure')
            else:
                return HttpResponse('success' if False else 'Undefined object form')
        elif action == 'update':
            form_kwargs = {'data': self.request.POST, 'files': self.request.FILES}
            if 'parent' in form_kwargs['data'] and form_kwargs['data']['parent'] == 'root':
                form_kwargs['data']['parent'] = None
            form_kwargs.update({'instance': self.get_object()})
            if self.form_type is not None and self.update is not None:
                form = self.form_type(**form_kwargs)
                success = self.update(form)
                return HttpResponse(json.dumps({'success': success, 'msg': 'success'}),
                                    content_type='application/json')
            else:
                return HttpResponse(json.dumps({'success': False, 'msg': 'Undefined object form'}),
                                    content_type='application/json')
        else:
            return super(SingleTreeEditorMixin).edit_handler(self, request, *arg, **kwargs)
