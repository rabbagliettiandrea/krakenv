# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from django.conf.urls import patterns, include


urlpatterns = patterns('',
    (r'^', include('allauth.urls')),
)