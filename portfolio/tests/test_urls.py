from portfolio import app
from portfolio.views import projects
from pyquery import PyQuery
from unittest import TestCase
from collections import Counter

class TestProjects(TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_home(self):

        resp = self.app.get('/')
        self.assertEqual(resp.status_code, 200)

        pq = PyQuery(resp.data)
        links = [a.attrib['href'] for a in pq('a[href]')]
        count = Counter(links)
        self.assertEqual(count['/#about'], 2)
        self.assertEqual(count['/#projects'], 2)
        self.assertEqual(count['/#contacts'], 2)
        for project in projects.all:
            self.assertEqual(count['/{}/'.format(project['key'])], 1)

    def test_projects(self):

        for project in projects.all:

            resp = self.app.get('/{}/'.format(project['key']))
            self.assertEqual(resp.status_code, 200)

            pq = PyQuery(resp.data)
            links = [a.attrib['href'] for a in pq('a[href]')]
            count = Counter(links)
            self.assertEqual(count['/#about'], 2)
            self.assertEqual(count['/#projects'], 2)
            self.assertEqual(count['/#contacts'], 2)

            suggestions = [a.attrib['href'] for a in pq('#suggestions a')]
            self.assertEqual(len(suggestions), 6)
            for suggestion in suggestions:
                self.assertIn(suggestion[1:-1], projects.order)
                self.assertNotEqual(suggestion[1:-1], project)

    def test_robots(self):
       resp = self.app.get('/robots.txt')
       self.assertEqual(resp.status_code, 200)
       self.assertEqual(resp.mimetype, 'text/plain')

    def test_sitemap(self):
        resp = self.app.get('/sitemap.xml')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.mimetype, 'application/xml')

    def test_favicons(self):

        resp = self.app.get('/favicon.ico')
        self.assertEqual(resp.status_code, 200)

        home = self.app.get('/')
        pq = PyQuery(home.data)
        favicons = list()
        for link in pq('link'):
            href = link.attrib['href']  
            if 'favicon' in href:
                favicons.append(href)
        for favicon in favicons:
            resp = self.app.get(favicon)
            self.assertEqual(resp.status_code, 200)
