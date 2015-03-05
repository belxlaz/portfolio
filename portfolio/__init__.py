# coding: utf-8
from flask import Flask
from flask.ext.assets import Environment
from flask.ext.compress import Compress
from flask.ext.script import Manager
from portfolio.views import site

# init the app, its compressor and its manager
app = Flask('portfolio')
manager = Manager(app)
Compress(app)

# config
app.config.from_pyfile('config.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# assets
assets = Environment(app)
assets.config['PYSCSS_LOAD_PATHS'] = app.config['PYSCSS_LOAD_PATH']
assets.load_path = app.config['WEBASSETS_LOAD_PATH']
assets.from_yaml(app.config['ASSETS'])

# load views
app.register_blueprint(site)
