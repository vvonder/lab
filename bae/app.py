#-*- coding:utf-8 -*-

import os
import sys

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
LIBS_ROOT = os.path.join(APP_ROOT, 'libs')
TEMPLATES_ROOT = os.path.join(APP_ROOT, 'templates')
STATIC_ROOT = os.path.join(APP_ROOT, 'static')
sys.path.insert(0, LIBS_ROOT)

import bottle
from bottle import Bottle, static_file
from bottle import mako_template as template

bottle.TEMPLATE_PATH.insert(0, TEMPLATES_ROOT)


app = Bottle()


@app.route('/')
@app.route('/<name>')
def hello(name="vvonder"):
    return template('index', **locals())


@app.route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root=STATIC_ROOT)


if 'SERVER_SOFTWARE' in os.environ:
    from bae.core.wsgi import WSGIApplication
    application = WSGIApplication(app)
else:
    from bottle import run
    run(app, host='0.0.0.0', reloader=True, debug=True)
