# -*- coding: utf-8 -*-
__author__ = 'dimitriy'
LOCAL_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'magmag',                      # Or path to database file if using sqlite3.
        'USER': 'postgres',                      # Not used with sqlite3.
        'PASSWORD': 'sps67',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

LOCAL_ADMINS = (
    ('Nikolaev Dimitriy', 'constructor3@yandex.ru'),
    )
LOCAL_EMAIL_SUBJECT_PREFIX = '[Pharm Markt] '
LOCAL_EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' #'django.core.mail.backends.smtp.EmailBackend'
LOCAL_EMAIL_HOST ='smtp.fullspace.ru'
LOCAL_EMAIL_HOST_USER = 'admin@evesdream.ru'
LOCAL_EMAIL_HOST_PASSWORD = 'sps67j7k'