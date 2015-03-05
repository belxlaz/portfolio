# coding: utf-8
import sys
from flask import abort, Blueprint, g, render_template
from portfolio.projects import Project

reload(sys)
sys.setdefaultencoding('utf-8')
site = Blueprint('site', __name__, static_folder='static')
projects = Project()


# home
@site.route('/')
def index():
    return render_template('home.html')


# project pages
@site.route('/<key>')
def portfolio(key):

    # check if project exists
    if not projects.exist(key):
        return abort(404)

    # load project info
    project = projects.get(key)
    g.title = project['title']
    g.keywords = project['keywords']
    g.cover = project['cover']

    # generate template variables
    template = '{}.html'.format(key)
    suggestions = projects.suggestion(key, 6)

    return render_template(template, project=project, suggestions=suggestions)


# seo and browser
@site.route('/robots.txt')
def robots():
    return site.send_static_file('robots.txt')


@site.route('/favicon.ico')
def favicon():
    return site.send_static_file('imgs/favicon/favicon.ico')


# title and seo info auto generator
@site.context_processor
def title():

    # basic values
    name = 'Mabel Lazzarin'
    about = "{}'s Portfolio | UX & Visual Designer".format(name)
    banner = 'cover.png'
    keywords = ['Mabel Lazzarin', 'ux designer', 'user experience designer',
                'visual designer', 'user experience', 'london']

    # load page specific values
    subtitle = g.get('title', None)
    title = '{} | {}'.format(subtitle, name) if subtitle else name
    description = '{} | {}'.format(subtitle, about) if subtitle else about
    [keywords.append(k) for k in g.get('keywords', [])]
    cover = g.get('cover', banner)

    # set page class
    page_class = 'home' if name == title else 'project'

    # return values
    return {'name': name,
            'title': title,
            'description': description,
            'cover': cover,
            'keywords': ', '.join(keywords),
            'page_class': page_class,
            'projects': projects}
