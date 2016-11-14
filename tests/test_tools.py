import unittest
from catkin_fetch.fetcher.tools import Tools


class TestTools(unittest.TestCase):

    def test_prepare_default_url(self):
        test_url = ''
        self.assertEqual(test_url, Tools.prepare_default_url(test_url))
        test_url_git = 'git@path/'
        self.assertEqual(test_url_git + '{package}' + '.git',
                         Tools.prepare_default_url(test_url_git))
        test_url_git = 'git@path'
        self.assertEqual(test_url_git + '/{package}' + '.git',
                         Tools.prepare_default_url(test_url_git))
        test_url_http = 'https://path/'
        self.assertEqual(test_url_http + '{package}',
                         Tools.prepare_default_url(test_url_http))
        test_url_http = 'https://path'
        self.assertEqual(test_url_http + '/{package}',
                         Tools.prepare_default_url(test_url_http))

    def test_decorate(self):
        self.assertEqual('[blah]', Tools.decorate('blah'))