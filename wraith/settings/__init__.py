# -*- coding: utf-8 -*-

import os
from importlib import import_module


STAGE = os.environ.get('ZILLA_STAGE')
local_settings = import_module('wraith.settings.%s' % STAGE)
globals().update(vars(local_settings))


for tentacle in globals()['TENTACLES'].itervalues():
    try:
        globals().update(vars(import_module('%s.settings' % tentacle.path)))
    except ImportError:
        pass