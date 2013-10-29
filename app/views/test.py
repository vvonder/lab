#-*- coding:utf-8 -*-

from bottle import mako_template as template
from bottle import request

from . import app


@app.route('/')
@app.route('/user/<name>')
def hello(name="vvonder"):
    return template('index', **locals())


@app.route('/test')
def test():
    s = request.environ.get('beaker.session')
    s['test'] = s.get('test', 0) + 1
    s.save()
    return 'Test conter: %d' % s['test']
