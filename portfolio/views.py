from flask import abort, Blueprint, g, render_template
from portfolio.projects import Project

site = Blueprint('site', __name__, static_folder='static')
projects = Project()


# home
@site.route('/')
def index():
    return render_template('home.html')


# project pages
@site.route('/<project>')
def project(project):

    # check if project exists
    if not projects.exist(project):
        return abort(404)

    # load project info
    g.title = projects[project]['title']
    g.keywords = [k.split() for k in projects[project]['keywords'].split(',')]
    template = '{}.html'.format(project)

    return render_template(template)


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
            'page_class': page_class,
            'projects': projects}
