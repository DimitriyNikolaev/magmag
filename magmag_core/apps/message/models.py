# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

from magmag_core.apps.base_models.base_message import AbstractEmailMessage, AbstractCallRequest


class ClientRequest(AbstractEmailMessage):
    pass


class CallRequest(AbstractCallRequest):
    pass