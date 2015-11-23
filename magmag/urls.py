# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from magmag_core.app import application
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from magmag import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'magmag.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'', include(application.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout$', logout,name='logout' ),
)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)