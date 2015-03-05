#!/home1/meiaduzi/venv/mabel/bin/python

from flup.server.fcgi import WSGIServer
from portfolio import app as application

WSGIServer(application).run()
