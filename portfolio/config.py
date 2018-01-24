from decouple import config
from os import pardir, path

# basic app settings
DEBUG = config('DEBUG', default=False, cast=bool)
ASSETS_DEBUG = config('ASSETS_DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY', default=False)

# directories and files
BASEDIR = path.dirname(path.abspath(__file__))
ROOT = path.abspath(path.join(BASEDIR, pardir))
PROJECTS = path.join(BASEDIR, 'projects.yml')

# webassets
ASSETS = path.join(BASEDIR, 'assets.yml')
PYSCSS_LOAD_PATH = [BOURBON, NEAT, SCSS]
NODE = path.join(ROOT, 'node_modules')
BOURBON = path.join(NODE, 'bourbon', 'app', 'assets', 'stylesheets')
NEAT = path.join(NODE, 'bourbon-neat', 'app', 'assets', 'stylesheets')
SCSS = path.join(NODE, 'scss')
WEBASSETS_LOAD_PATH = [NODE, BASEDIR]
COFFEE_BIN = config('COFFEE_BIN', default=False)

# freezer
FREEZER_REMOVE_EXTRA_FILES = True

# google analytics user id
GOOGLE_ANALYTICS = config('GOOGLE_ANALYTICS', default=False)
INSERT_GOOGLE_ANALYTICS = GOOGLE_ANALYTICS and not DEBUG
