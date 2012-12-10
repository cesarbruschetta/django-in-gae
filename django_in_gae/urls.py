# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from app.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^hello/$', helloword, name='HelloWord'),
    url(r'^cidade/([^\s]+)/$', capitais, name="Capitais"),
    
    
    # url(r'^django_in_gae/', include('django_in_gae.foo.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # URL de arquivos staticos
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
