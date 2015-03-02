from decouple import config
from os import path

# basic app settings
DEBUG = config('DEBUG', default=False, cast=bool)
ASSETS_DEBUG = config('ASSETS_DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY', default=False)

# directories and files
BASEDIR = path.dirname(path.abspath(__file__))
PROJECTS = path.join(BASEDIR, 'projects.yml')

# webassets
ASSETS = path.join(BASEDIR, 'assets.yml')
STATIC = path.join(BASEDIR, 'static')
BOURBON = path.join(STATIC, 'bower/bourbon/app/assets/stylesheets')
NEAT = path.join(STATIC, 'bower/neat/app/assets/stylesheets')
SCSS = path.join(STATIC, 'scss')
PYSCSS_LOAD_PATH = [BOURBON, NEAT, SCSS]
WEBASSETS_LOAD_PATH = [STATIC]
