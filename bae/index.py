#-*- coding:utf-8 -*-

import os
import sys

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
LIBS_ROOT = os.path.join(APP_ROOT, 'libs')
TEMPLATES_ROOT = os.path.join(APP_ROOT, 'templates')
sys.path.insert(0, LIBS_ROOT)

DEV = False

import bottle
from bottle import Bottle
from bottle import mako_template as template

bottle.TEMPLATE_PATH.insert(0, TEMPLATES_ROOT)


app = Bottle()


@app.route('/')
@app.route('/<name>')
def hello(name="vvonder"):
    return template('index', **locals())


if DEV:
    from bottle import run
    run(app, host='0.0.0.0')
else:
    from bae.core.wsgi import WSGIApplication
    application = WSGIApplication(app)
