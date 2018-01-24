from flask import Flask
from flask_assets import Environment
from whitenoise import WhiteNoise

from portfolio.views import site

# init the app
app = Flask('portfolio')
app.wsgi_app = WhiteNoise(app.wsgi_app, root='static/')

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

@app.cli.command(help='Compress static files.')
def compress():
    import os
    import shutil
    from whitenoise.compress import main
    shutil.rmtree(os.path.join('portfolio', 'static', '.webassets-cache'))
    main(os.path.join('portfolio', 'static'))
