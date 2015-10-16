# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
import krakenv.thread


class KrakenvRouter(object):

    def _route(self, model, **hints):
        try:
            return krakenv.thread.local.tentacle.database
        except AttributeError:
            raise RuntimeError('No DB selected')

    def db_for_read(self, model, **hints):
        return self._route(model, **hints)

    def db_for_write(self, model, **hints):
        return self._route(model, **hints)
