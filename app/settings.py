#-*- coding:utf-8 -*-

import os
import sys

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
LIBS_ROOT = os.path.join(APP_ROOT, 'libs')
TEMPLATES_ROOT = os.path.join(APP_ROOT, 'templates')
STATIC_ROOT = os.path.join(APP_ROOT, 'static')
sys.path.insert(0, LIBS_ROOT)

DEBUG = True
DB_URL = 'sqlite:///:memory:'  # test, in mem

SESSION_OPTIONS = {
    'session.type': 'ext:database',
    'session.url': DB_URL,
    'session.data_dir': '/tmp',
    'session.coolie_expires': True,
    'session.timeout': 3600 * 24,
    'session.encrypt_key': 'encrypt_key',
    'session.validate_key': 'validate_key',
}
