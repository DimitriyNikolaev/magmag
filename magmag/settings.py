"""
Django settings for magmag project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from magmag_core import MAGMAG_MAIN_TEMPLATE_DIR
from magmag_core import get_core_apps
from magmag.local_settings import LOCAL_DATABASES, LOCAL_ADMINS, LOCAL_MANAGERS, LOCAL_EMAIL_BACKEND, LOCAL_EMAIL_HOST,\
    LOCAL_EMAIL_HOST_USER,LOCAL_EMAIL_HOST_PASSWORD, LOCAL_EMAIL_SUBJECT_PREFIX

location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#p17&g643jd7o+dt#*gcj5z&rc!=_(0^#5bo3fqd2%qnmj4hsa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SEND_BROKEN_LINK_EMAILS = False
ADMINS = LOCAL_ADMINS
MANAGERS = LOCAL_MANAGERS
EMAIL_SUBJECT_PREFIX = LOCAL_EMAIL_SUBJECT_PREFIX
EMAIL_BACKEND = LOCAL_EMAIL_BACKEND #'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = LOCAL_EMAIL_HOST
EMAIL_HOST_USER = LOCAL_EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = LOCAL_EMAIL_HOST_PASSWORD
# Application definition

INSTALLED_APPS = ['django.contrib.admin',
                  'django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django.contrib.messages',
                  'django.contrib.staticfiles'
                  ]
INSTALLED_APPS = INSTALLED_APPS + get_core_apps()

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'magmag.urls'

WSGI_APPLICATION = 'magmag.wsgi.application'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django_mobile.loader.Loader'
    #django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (MAGMAG_MAIN_TEMPLATE_DIR, )
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = LOCAL_DATABASES

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'ru'
LANGUAGES = (('ru', 'Russian'),	('en', 'English'),)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = location('static')
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

MEDIA_ROOT = location('media')
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
    'magmag_core.core.context_processors.user_metadata',
    'django.core.context_processors.i18n',
    #'django_mobile.context_processors.flavour'
    )

#custom
APPLICATION_NAME = "MAGMAG"
SITE_DOMAIN = 'http://evesdream.ru'


#preview images
PREVIEW_IMG__WIDTH = 498
PREVIEW_IMG_HEIGHT = 372

THUMBNAIL_WIDTH = 150
THUMBNAIL_HEIGHT = 150

# if DEBUG:
#     MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
#     INSTALLED_APPS += ('debug_toolbar',)
#     DEBUG_TOOLBAR_PANELS = (
#         #'debug_toolbar.panels.version.VersionDebugPanel',
#         'debug_toolbar.panels.timer.TimerPanel',
#         'debug_toolbar.panels.settings.SettingsPanel',
#         'debug_toolbar.panels.headers.HeadersPanel',
#         'debug_toolbar.panels.request.RequestPanel',
#         'debug_toolbar.panels.sql.SQLPanel',
#         'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#         'debug_toolbar.panels.templates.TemplatesPanel',
#         'template_timings_panel.panels.TemplateTimings.TemplateTimings',
#         'debug_toolbar.panels.cache.CachePanel',
#         'debug_toolbar.panels.signals.SignalsPanel',
#         'debug_toolbar.panels.logging.LoggingPanel',
#         'debug_toolbar.panels.redirects.RedirectsPanel',
#     )
#     DEBUG_TOOLBAR_CONFIG = {
#         'EXCLUDE_URLS': ('/admin',),
#         'INTERCEPT_REDIRECTS': False,
#     }
