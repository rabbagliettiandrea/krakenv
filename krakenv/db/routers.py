# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
import krakenv.thread


class KrakenvRouter(object):

    def _route(self, model, **hints):
        tentacle = getattr(krakenv.thread.local, 'tentacle', None)
        if tentacle:
            return tentacle.database

    def db_for_read(self, model, **hints):
        return self._route(model, **hints)

    def db_for_write(self, model, **hints):
        return self._route(model, **hints)
