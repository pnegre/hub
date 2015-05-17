# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns('',

    (r'^$', 'hub.views.index'),
    (r'^menu$', 'hub.views.menu'),

)
