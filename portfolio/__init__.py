from flask import abort, Flask, g, render_template, send_from_directory
from flask.ext.assets import Environment
from flask.ext.compress import Compress
from flask.ext.script import Manager
from portfolio.projects import Project

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

# load projects
projects = Project()


# home
@app.route('/')
def index():
    return render_template('home.html', projects=projects)


# project pages
@app.route('/<project>')
def project(project):

    # check if project exists
    if project not in projects.keys():
        abort(404)

    # load project info
    g.title = projects[project]['title']
    g.keywords = [k.split() for k in projects[project]['keywords'].split(',')]
    template = '{}.html'.format(project)

    return render_template(template)


# seo and browser
@app.route('/robots.txt')
def robots():
    return send_from_directory(static, 'robots.txt')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(path.join(static, 'imgs', 'favicon'), 'favicon.ico')


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
