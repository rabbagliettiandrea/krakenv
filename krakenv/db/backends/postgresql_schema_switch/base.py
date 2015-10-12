# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from django.db.backends.postgresql_psycopg2.base import DatabaseWrapper as PostgresqlPsycopg2DatabaseWrapper


class DatabaseWrapper(PostgresqlPsycopg2DatabaseWrapper):

    def cursor(self):
        cursor = super(PostgresqlPsycopg2DatabaseWrapper, self).cursor()
        cursor.execute('SET search_path=%s' % self.settings_dict.get('SCHEMA', 'public'))
        return cursor
