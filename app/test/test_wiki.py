import unittest
from unittest.mock import patch

from app.api.wiki import Wiki

WIKI_DATA_PAGE = {'batchcomplete': '', 'query': {'geosearch': [
    {'pageid': 10142861, 'ns': 0, 'title': 'Facebook City', 'lat': 37.481027, 'lon': -122.153898, 'dist': 439.5,
     'primary': ''}]}}

WIKI_DATA_DESC = {'batchcomplete': '', 'query': {'pages': {
    '10142861': {'pageid': 10142861, 'ns': 0, 'title': 'Facebook City',
                 'extract': "Facebook City ou Zee-Town (Ville Facebook, ou Ville Z, comme Zuckerberg) est un "
                            "important projet de création de ville nouvelle-campus urbanisé-cité idéale d'environ 80 "
                            "hectares. Ce projet est lancé en 2012 par Mark Zuckerberg, PDG fondateur de la société "
                            "américaine de réseautage social Facebook (entreprise), à Menlo Park, dans la baie de San "
                            "Francisco, de la Silicon Valley, en Californie, aux États-Unis,."}}}}


class MockResponsePage:
    """
    Return json expected pages
    """
    def json(self):
        return WIKI_DATA_PAGE


class MockResponseDesc:
    """
    Return json expected description
    """
    def json(self):
        return WIKI_DATA_DESC


class TestWiki(unittest.TestCase):
    """
    Class test for the Wikipedia class.
    """

    def setUp(self):
        self.lat = 37.4835791
        self.lng = -122.1500939
        self.url = "https://fr.wikipedia.org/w/api.php"

    def test_get_page(self):
        params = {
            "action": "query",
            "list": "geosearch",
            "gsradius": 1000,
            "gscoord": "%s|%s" % (self.lat, self.lng),
            "format": "json",
        }
        with patch('app.api.wiki.requests.get') as mock_requests:
            wiki = Wiki(self.lat, self.lng)
            mock_requests.return_value = MockResponsePage()
            results = wiki.get_page()
            self.assertEqual(results, WIKI_DATA_PAGE["query"]["geosearch"][0]['pageid'])
            mock_requests.assert_called_once_with(self.url, params=params)

    def test_get_description(self):
        params = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "exintro": "1",
            "explaintext": "1",
            "exsentences": "5",
            "pageids": 10142861
        }
        with patch('app.api.wiki.requests.get') as mock_requests:
            wiki = Wiki(self.lat, self.lng)
            mock_requests.return_value = MockResponseDesc()
            wiki.page = WIKI_DATA_PAGE["query"]["geosearch"][0]['pageid']
            results = wiki.get_description()
            self.assertEqual(results, WIKI_DATA_DESC["query"]["pages"][str(wiki.page)]["extract"])
            mock_requests.assert_called_once_with(self.url, params=params)
