# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division
from django.conf import settings
from django.utils import timezone


def get__settings(request):
    return {'settings': lambda: settings}


def get__datetime_now(request):
    return {'datetime_now': lambda: timezone.localtime(timezone.now())}


def get__user_is_logged(request):
    return {'user_is_logged': lambda: request.user.is_authenticated() and not request.user.is_staff}