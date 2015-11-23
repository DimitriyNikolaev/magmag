# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

from django import forms
from magmag_core.apps.message.models import ClientRequest, CallRequest


class ClientRequestForm(forms.ModelForm):
    class Meta:
        model = ClientRequest
        exclude = ['viewed', 'data']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'mail@example.com', 'id': 'client_request_email'})
        }


class CallRequestForm(forms.ModelForm):
    class Meta:
        model = CallRequest
        exclude = ['viewed', 'data']
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': '+7(905)-273-56-99', 'id': 'call_request_phone'})
        }


class CallRequestFullForm(forms.ModelForm):
    class Meta:
        model = CallRequest


class ClientRequestFullForm(forms.ModelForm):
    class Meta:
        model = ClientRequest

