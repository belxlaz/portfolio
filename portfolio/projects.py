import os
import yaml


class Project(object):

    def __init__(self, path='projects.yml', root=False):

        # main veriables
        self.all = dict()
        self.order = list()
        
        # set root
        if not root or not os.path.isdir(root):
            root = os.path.dirname(os.path.abspath(__file__))

        # load projects
        full_path = os.path.join(root, path)
        if os.path.isfile(full_path):
            with open(full_path) as file_handler:
                self.order = self.__get_order(file_handler)
                file_handler.seek(0)
                self.all = yaml.load(file_handler.read())

        # convert keywords to list
        if self.all:
            for key in self.all.keys():
                project = self.all[key]
                parsed = [k.strip() for k in project['keywords'].split(',')]
                project['keywords'] = parsed

    def get(self, key):
        if self.all:
            output = self.all.get(key, None)
            if output:
                output['key'] = key
            return output
        return None

    def filter(self, keyword):
        output = list()
        for key in self.order:
            project = self.all[key]
            if keyword in project['keywords']:
                output.append(key)
        return output

    def __get_order(self, file_handler):
        output = list()
        for line in file_handler:
            if line[0:1].isalpha():
                output.append(line[0:line.index(':')].strip())
        return output
