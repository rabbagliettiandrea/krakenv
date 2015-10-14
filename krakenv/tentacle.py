# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from django.conf import settings


class Tentacle(object):

    def __init__(self, path, database):
        self.path = path
        self.database = database

    @staticmethod
    def get_tentacle(request):
        domain = request.get_host().partition(':')[0]
        return settings.TENTACLES.get(domain)