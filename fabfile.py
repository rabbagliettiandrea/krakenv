# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from fabric.api import env
from fabric.contrib import django as fab_django
from fabric.decorators import task
from fabric.operations import local, os

fab_django.settings_module('krakenv.settings')
from django.conf import settings

env.key_filename = getattr(settings, 'RSA_FILEPATH')
env.celery_app = 'celery_app'

from django_zilla.fabric_tasks import queue, misc, git, db, migrations
