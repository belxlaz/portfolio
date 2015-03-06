# coding: utf-8

from functools import wraps
from htmlmin import minify


def minified(html_content):
    @wraps(html_content)
    def minify_it():
        return minify(html_content(), remove_comments=True)
    return minify_it
