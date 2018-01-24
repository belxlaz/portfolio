from flask import Flask
from flask_assets import Environment
from portfolio.views import site

# init the app, its compressor and its manager
app = Flask('portfolio')

# config
app.config.from_pyfile('config.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# assets
assets = Environment(app)
assets.config['LIBSASS_INCLUDES'] = app.config['LIBSASS_INCLUDES']
assets.config['coffeescript_bin'] = app.config['COFFEE_BIN']
assets.load_path = app.config['WEBASSETS_LOAD_PATH']
assets.from_yaml(app.config['ASSETS'])

# load views
app.register_blueprint(site)
