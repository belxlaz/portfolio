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
SRC = path.join(BASEDIR, 'src')
BOURBON = path.join(SRC, 'bower/bourbon/app/assets/stylesheets')
NEAT = path.join(SRC, 'bower/neat/app/assets/stylesheets')
SCSS = path.join(SRC, 'scss')
PYSCSS_LOAD_PATH = [BOURBON, NEAT, SCSS]
WEBASSETS_LOAD_PATH = [SRC]
COFFEE_BIN = config('COFFEE_BIN', default=False)

# google analytics user id
GOOGLE_ANALYTICS = config('GOOGLE_ANALYTICS', default=False)
INSERT_GOOGLE_ANALYTICS = GOOGLE_ANALYTICS and not DEBUG

# error logging
LOG = path.join(path.dirname(BASEDIR), 'errors.log')
