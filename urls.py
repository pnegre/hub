# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('',

        (r'^$', 'hub.views.index'),
        (r'^menu$', 'hub.views.menu'),

)
