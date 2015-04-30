from flask import Flask
from flask.ext.assets import Environment
from flask.ext.frozen import Freezer
from flask.ext.script import Manager
from portfolio.views import site

# init the app, its compressor and its manager
app = Flask('portfolio')
manager = Manager(app)

# config
app.config.from_pyfile('config.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# assets
assets = Environment(app)
assets.config['PYSCSS_LOAD_PATHS'] = app.config['PYSCSS_LOAD_PATH']
assets.config['coffeescript_bin'] = app.config['COFFEE_BIN']
assets.load_path = app.config['WEBASSETS_LOAD_PATH']
assets.from_yaml(app.config['ASSETS'])

# load views
app.register_blueprint(site)

# freezer
FreezerCommand = Manager(usage='Frozen-Flask commands')


@FreezerCommand.command
def freeze():
    """Freeze Flask application"""
    freezer = Freezer(app)
    freezer.freeze()

manager.add_command('freezer', FreezerCommand)
