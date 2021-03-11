import unittest
from unittest.mock import patch

from app.api.wiki import Wiki


class TestWiki(unittest.TestCase):
    """
    Class test for the Wikipedia class.
    """

    def setUp(self):
        self.lat = 37.4835791
        self.lng = -122.1500939

        self.expected_page = 10142861

        self.expected_description = "Facebook City ou Zee-Town (Ville Facebook, ou Ville Z, comme Zuckerberg) est un " \
                                    "important projet de création de ville nouvelle-campus urbanisé-cité idéale " \
                                    "d'environ 80 hectares. Ce projet est lancé en 2012 par Mark Zuckerberg, " \
                                    "PDG fondateur de la société américaine de réseautage social Facebook (" \
                                    "entreprise), à Menlo Park, dans la baie de San Francisco, de la Silicon Valley, " \
                                    "en Californie, aux États-Unis,. "

        self.wiki = Wiki(self.lat, self.lng)


    @patch.object(Wiki, "get_page")
    def test_get_page(self, mock_request):
        mock_request.return_value = self.expected_page
        mock_request.get.return_value.status_code = 200

        results = self.wiki.get_page()
        self.assertEqual(results, self.expected_page)
        mock_request.assert_called_once_with(self.lat, self.lng)

    @patch.object(Wiki, "get_description")
    def test_get_page(self, mock_request):
        mock_request.return_value = self.expected_description
        results = self.wiki.get_description()
        self.assertEqual(results, self.expected_description)



