# -*- coding: utf-8 -*-
__author__ = 'dimitriy'

from django.conf import settings
from django.core.mail import send_mail


def send_email(title, msg, to):
    send_mail(title,msg, settings.EMAIL_HOST_USER,to)