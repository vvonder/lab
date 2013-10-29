#-*- coding:utf-8 -*-

import os

import bottle
from beaker.middleware import SessionMiddleware

import settings
from views import app

bottle.TEMPLATE_PATH.insert(0, settings.TEMPLATES_ROOT)


@app.route('/static/<filename:path>')
def send_static(filename):
    return bottle.static_file(filename, root=settings.STATIC_ROOT)

app = SessionMiddleware(app, settings.SESSION_OPTIONS)

if 'SERVER_SOFTWARE' in os.environ:
    from bae.core.wsgi import WSGIApplication
    application = WSGIApplication(app)
else:
    from bottle import run
    run(app, host='0.0.0.0', reloader=True, debug=True)
