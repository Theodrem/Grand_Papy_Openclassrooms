import unittest
from unittest.mock import Mock

from app.api.wiki import Wiki


class TestWiki(unittest.TestCase):
    """
    Class test for the Wikipedia class.
    """

    def setUp(self):
        """
        Unittest setup
        """
        self.wiki = Wiki(37.4835791, -122.1500939)
        self.wiki.get_page = Mock()
        self.wiki.get_description = Mock()
        self.result_page = {'batchcomplete': '',
                            'query': {'geosearch': [{'pageid': 10142861,
                                                     'ns': 0, 'title': 'Facebook City', 'lat': 37.481027,
                                                     'lon': -122.153898, 'dist': 439.5, 'primary': ''}]}}
        self.result_description = {'batchcomplete': '',
                                   'query':
                                       {'pages':
                                            {'10142861':
                                                 {'pageid': 10142861, 'ns': 0, 'title': 'Facebook City',
                                                  'extract': "Facebook City ou Zee-Town (Ville Facebook, "
                                                             "ou Ville Z, comme Zuckerberg) est un "
                                                             "important projet de création de ville "
                                                             "nouvelle-campus urbanisé-cité idéale "
                                                             "d'environ 80 hectares. Ce projet est lancé "
                                                             "en 2012 par Mark Zuckerberg, PDG fondateur "
                                                             "de la société américaine de réseautage "
                                                             "social Facebook (entreprise), "
                                                             "à Menlo Park, dans la baie de San "
                                                             "Francisco, de la Silicon Valley, "
                                                             "en Californie, aux États-Unis,."}}}}

    def test_get_page(self):
        """
        :return: Data to false request.
        """
        self.wiki.get_page.return_value = self.result_page["query"]["geosearch"][0]['pageid']
        self.assertEqual(self.wiki.get_page(), 10142861)
