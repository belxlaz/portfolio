# coding: utf-8

from flask import render_template
from htmlmin import minify


def render_minified(*args, **kwargs):
    return minify(render_template(*args, **kwargs), remove_comments=True)
