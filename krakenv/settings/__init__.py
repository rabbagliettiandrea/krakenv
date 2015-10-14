# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from importlib import import_module

import os

from .core import *
from wraith import settings as wraith_settings

STAGE = os.environ.get('ZILLA_STAGE')
local_settings = import_module('wraith.settings.%s' % STAGE)
globals().update(vars(local_settings))

TENTACLES = wraith_settings.TENTACLES
INSTALLED_APPS += wraith_settings.APPS + [tentacle.path for tentacle in TENTACLES.itervalues()]


for tentacle in TENTACLES.itervalues():
    try:
        globals().update(vars(import_module('%s.settings' % tentacle.path)))
    except ImportError:
        pass