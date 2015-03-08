# coding: utf-8

try:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
except NameError:
    pass

from flask import abort, Blueprint, g, make_response, render_template
from portfolio.minify import render_minified
from portfolio.projects import Project
from portfolio.sitemap import Sitemap

site = Blueprint('site', __name__, static_folder='static')
projects = Project()


# home
@site.route('/')
def index():
    return render_minified('home.html', projects=projects.ordered())


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

    return render_minified('{}.html'.format(key),
                           project=project,
                           suggestions=projects.suggestion(key, 6))


# seo and browser
@site.route('/robots.txt')
def robots():
    return site.send_static_file('robots.txt')


@site.route('/sitemap.xml')
def sitemap():
    info = Sitemap(project_list=projects.order)
    xml = render_template('sitemap.xml', pages=info.pages)
    response = make_response(xml)
    response.headers['Content-Type'] = 'application/xml'
    return response


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
            'page_class': page_class}
