import os
import yaml
import random


class Project(object):

    def __init__(self, path='projects.yml', root=False):

        # main veriables
        self.raw = dict()
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
                self.raw = yaml.load(file_handler.read())

        # convert keywords to list
        if self.raw:
            for key in self.raw.keys():
                project = self.raw[key]
                parsed = [k.strip() for k in project['keywords'].split(',')]
                project['keywords'] = parsed

        # order all projects in one list
        self.all = self.ordered()

    def get(self, key):
        if self.raw:
            output = self.raw.get(key, None)
            if output:
                output['key'] = key
            return output
        return None

    def ordered(self, keys=False):
        if not keys:
            keys = self.order
        return [self.get(k) for k in keys]

    def exist(self, key):
        if self.raw:
            if key in self.raw.keys():
                return True
        return False

    def filter(self, keyword):
        output = list()
        if self.raw:
            for key in self.order:
                if keyword in self.raw[key]['keywords']:
                    output.append(key)
        return output

    def suggestion(self, key, limit=False):

        # get all suggestions
        filtered = list()
        if self.raw:
            for keyword in self.raw[key]['keywords']:
                for project in self.filter(keyword):
                    if project not in filtered and project != key:
                        filtered.append(project)
        if not limit:
            limit = len(filtered)

        # randomize and crop
        output = self.__shuffle(filtered, limit)

        # complete with other categories (if needed)
        if len(output) < limit:
            remaining = limit - len(output)
            alternatives = list(set(self.order) - set(output))
            output.extend(self.__shuffle(alternatives, remaining))
            output = self.__shuffle(output)

        return self.ordered(output)

    @staticmethod
    def __shuffle(source, limit=False):
        output = list()
        source_copy = list(set(source))
        if not limit:
            limit = len(source_copy)
        while len(output) < limit:
            choosen = random.choice(source_copy)
            output.append(choosen)
            source_copy.remove(choosen)
            if not len(source_copy):
                break
        return output

    def __get_order(self, file_handler):
        output = list()
        for line in file_handler:
            if line[0:1].isalpha():
                output.append(line[0:line.index(':')].strip())
        return output
