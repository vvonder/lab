#-*- coding:utf-8 -*-

from bottle import mako_template as template
from bottle import request, redirect

from . import app

from models.user import User


@app.route('/')
@app.route('/user/<name>')
def hello(name="vvonder"):
    return template('index', **locals())


@app.route('/user/<name>/add')
def add_user(name, db):
    user = User(name=name, description="I'm %s" % name, type=1)
    db.add(user)
    return redirect(app.get_url('show_user', name=name))


@app.route('/user/<name>/show', name='show_user')
def show_user(name, db):
    user = db.query(User).first()
    if user:
        return '%s "%s"' % (user.name, user.description)


@app.route('/test')
def test():
    s = request.environ.get('beaker.session')
    s['test'] = s.get('test', 0) + 1
    s.save()
    return 'Test conter: %d' % s['test']
