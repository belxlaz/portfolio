from flask import Flask, g, render_template, send_from_directory
from flask.ext.assets import Environment
from flask.ext.compress import Compress
from flask.ext.script import Manager
from decouple import config
from unipath import Path

# init the app, its compressor and its manager
app = Flask(__name__)
manager = Manager(app)
Compress(app)

# config
app.config['DEBUG'] = config('DEBUG', default=False, cast=bool)
app.config['ASSETS_DEBUG'] = config('ASSETS_DEBUG', default=False, cast=bool)
app.config['SECRET_KEY'] = config('SECRET_KEY', default=False)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# assets
root = Path(__file__).parent
static = root.child('static')
bourbon = static.child('bower', 'bourbon', 'app', 'assets', 'stylesheets')
neat = static.child('bower', 'neat', 'app', 'assets', 'stylesheets')
scss = static.child('scss')
assets = Environment(app)
assets.config['PYSCSS_LOAD_PATHS'] = [bourbon.absolute(),
                                      neat.absolute(),
                                      scss.absolute()]
assets.load_path = [static]
assets.from_yaml(root.child('assets.yml'))


# home
@app.route('/')
def index():
    return render_template('home.html')


# seo and browser
@app.route('/robots.txt')
def robots():
    return send_from_directory(static, 'robots.txt')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(static.child('imgs', 'favicon'), 'favicon.ico')


# title and seo info auto generator
@app.context_processor
def title():

    # basic values
    name = 'Mabel Lazzarin'
    about = "{}'s Portfolio | UX & Visual Designer".format(name)
    keywords = ['Mabel Lazzarin', 'ux designer', 'user experience designer',
                'visual designer', 'user experience', 'london']

    # load page specific values
    subtitle = g.get('title', None)
    title = '{} | {}'.format(subtitle, name) if subtitle else name
    description = '{} | {}'.format(subtitle, about) if subtitle else about
    [keywords.append(k) for k in g.get('keywords', [])]
    banner = g.get('banner', 'file.png')

    # set page class
    page_class = 'home' if name == title else 'project'

    # return values
    return {'name': name,
            'title': title,
            'description': description,
            'keywords': ', '.join(keywords),
            'banner': banner,
            'page_class': page_class}

manager.run()
