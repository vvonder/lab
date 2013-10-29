#-*- coding:utf-8 -*-

import os
import sys

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
LIBS_ROOT = os.path.join(APP_ROOT, 'libs')
TEMPLATES_ROOT = os.path.join(APP_ROOT, 'templates')
STATIC_ROOT = os.path.join(APP_ROOT, 'static')
sys.path.insert(0, LIBS_ROOT)

SESSION_OPTIONS = {
    'session.type': 'cookie',
    'session.validate_key': True,
}
