# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from krakenv.tentacle import Tentacle
import krakenv.thread


class TentacleDispatcherMiddleware(object):

    def process_request(self, request):
        tentacle = Tentacle.get_tentacle(request)
        if tentacle:
            krakenv.thread.local.tentacle = tentacle
            request.urlconf = tentacle.path + '.urls'

    def process_response(self, request, response):
        if hasattr(krakenv.thread.local, 'tentacle'):
            del krakenv.thread.local.tentacle
        return response

    def process_exception(self, request, exception):
        if hasattr(krakenv.thread.local, 'tentacle'):
            del krakenv.thread.local.tentacle
