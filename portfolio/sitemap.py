# coding: utf-8

from datetime import datetime
from os import path, walk


class Sitemap(object):

    def __init__(self, project_list=[]):

        # set projects
        self.project_list = project_list

        # get all files
        self.files = list()
        directory = path.dirname(path.abspath(__file__))
        for root, dirs, files in walk(directory):
            self.files.extend([path.join(root, f) for f in files])

        # get all pages
        self.pages = self.home() + self.projects()

    def home(self):
        return [{'url': '', 'date': self.__last_update(), 'priority': 1}]

    def projects(self):
        output = list()
        for p in self.project_list:
            info = {'url': p, 'date': self.__last_update(p), 'priority': 0.8}
            output.append(info)
        return output

    def __last_update(self, project=False):
        files = self.files
        if project:
            files = [f for f in self.files if project in f[f.rfind('/'):]]
        last_change = 0
        for f in files:
            f_last_change = path.getmtime(f)
            if f_last_change > last_change:
                last_change = f_last_change
        return datetime.fromtimestamp(last_change).strftime('%Y-%m-%d')
