"""
Django settings for magmag project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from magmag.local_settings import LOCAL_DATABASES
from magmag_core import MAGMAG_MAIN_TEMPLATE_DIR
from magmag_core import get_core_apps

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


# Application definition

INSTALLED_APPS = ['django.contrib.admin',
                  'django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django.contrib.messages',
                  'django.contrib.staticfiles',
                  'south'
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

TEMPLATE_DIRS = (
    MAGMAG_MAIN_TEMPLATE_DIR
)
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = LOCAL_DATABASES

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = location('static')
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
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
