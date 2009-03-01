# coding: utf-8

from django.conf.urls.defaults import *
from noticias.views import principal

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^demo_estat/', include('demo_estat.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    
    (r'^$', principal)
)


# Para servir arquivos estáticos em ambiente de desenvolvimento

import sys
from django.conf import settings

if 'runserver' in sys.argv:
    import os
    urlpatterns += patterns('',
        (r'^estat/(.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(settings.PROJECT_PATH, 'estaticos')}
        ),
    )
