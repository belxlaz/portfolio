import os
from portfolio import app
from portfolio.projects import Project
from unittest import TestCase


class TestProjects(TestCase):

    def setUp(self):

        # test client
        app.config['TESTING'] = True
        self.app = app.test_client()

        # load projects
        root = os.path.dirname(os.path.abspath(__file__))
        self.projects = Project(path='test.yml', root=root)

        # support vars
        self.keys = ['twitch', 'clubsoda', 'trend']
        self.properties = ['title', 'tagline', 'keywords', 'cover']

    def test_raw(self):
        self.assertIsInstance(self.projects.raw, dict)
        self.assertEqual(len(self.projects.raw), 3)
        for key in self.keys:
            project = self.projects.raw.get(key, False)
            self.assertTrue(project)
            for property in self.properties:
                value = project.get(property, False)
                self.assertTrue(value)
                if property is 'keywords':
                    self.assertIsInstance(value, list)
                else:
                    self.assertIsInstance(value, str)

    def test_order(self):
        self.assertEqual(self.keys, self.projects.order)

    def test_all(self):
        self.assertIsInstance(self.projects.all, list)
        self.assertEqual(self.keys, [p['key'] for p in self.projects.all])
        for project in self.projects.all:
            self.assertIn(project['key'], self.keys)
            for property in self.properties + ['key']:
                value = project.get(property, False)
                self.assertTrue(value)
                if property is 'keywords':
                    self.assertIsInstance(value, list)
                else:
                    self.assertIsInstance(value, str)
   
    def test_project(self):

        twitch = self.projects.get('twitch')
        self.assertEqual(twitch['title'], 'Twitch – The Next Level')
        self.assertEqual(twitch['tagline'], 'Let users view & upload walkthroughs')
        self.assertEqual(twitch['keywords'], ['ux', 'graphic'])
        self.assertEqual(twitch['cover'], 'projects-twitch.jpg')

        clubsoda = self.projects.get('clubsoda')
        self.assertEqual(clubsoda['title'], 'Club Soda')
        self.assertEqual(clubsoda['tagline'], 'Social network to stop')
        self.assertEqual(clubsoda['keywords'], ['ux', 'graphic'])
        self.assertEqual(clubsoda['cover'], 'projects-clubsoda.jpg')

        trend = self.projects.get('trend')
        self.assertEqual(trend['title'], 'Trend Report')
        self.assertEqual(trend['tagline'], 'Designing future scenarios')
        self.assertEqual(trend['keywords'], ['trend'])
        self.assertEqual(trend['cover'], 'projects-trend.jpg')

        self.assertIsNone(self.projects.get('xpto'))

    def test_exist(self):
        for key in self.keys:
            self.assertTrue(self.projects.exist(key))
        for false_key in self.properties:
            self.assertFalse(self.projects.exist(false_key))

    def test_filter(self):

        trend = self.projects.filter('trend')
        self.assertEqual(trend, ['trend'])

        ux = self.projects.filter('ux')
        self.assertEqual(len(ux), 2)
        self.assertIn('twitch', ux)
        self.assertIn('clubsoda', ux)

        graphic = self.projects.filter('graphic')
        self.assertIn('twitch', graphic)
        self.assertIn('clubsoda', graphic)

        self.assertFalse(self.projects.filter('xpto'))
        
    def test_suggestion(self):

        for_clubsoda = self.projects.suggestion('clubsoda')
        self.assertIn(self.projects.get('twitch'), for_clubsoda)

        for_twitch = self.projects.suggestion('twitch', 2)
        self.assertIsInstance(for_twitch, list)
        self.assertEqual(len(for_twitch), 2)
        self.assertIn(self.projects.get('clubsoda'), for_twitch)
        self.assertIn(self.projects.get('trend'), for_twitch)
        self.assertNotIn(self.projects.get('twitch'), for_twitch)

        for_trend = self.projects.suggestion('trend')
        self.assertIsInstance(for_trend, list)
        self.assertEqual(len(for_trend), 2)
