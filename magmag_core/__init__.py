# -*- coding: utf-8 -*-
__author__ = 'dimitriy'
import os

MAGMAG_CORE_APPS = [
    'magmag_core',
    'magmag_core.apps.account',
    'magmag_core.apps.catalogue',
    'magmag_core.apps.order',
    'magmag_core.apps.pages',
    'magmag_core.apps.promo',
    'magmag_core.apps.message',
    'magmag_core.apps.dashboard',
    'magmag_core.apps.dashboard.dashboard_catalogue',
    'magmag_core.apps.dashboard.dashboard_order',
    'magmag_core.apps.dashboard.dashboard_pages'
]


def get_core_apps():
    return MAGMAG_CORE_APPS

MAGMAG_MAIN_TEMPLATE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'templates')