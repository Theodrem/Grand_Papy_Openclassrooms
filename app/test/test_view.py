import unittest
import mock
import os
from mock import patch

from app.api.geocoding import Geocoding
from app.api.wiki import Wiki
from app.parser import Parser
from app import app

GEOCODING_DATA = {
    'results': [{'address_components': [{'long_name': '10', 'short_name': '10', 'types': ['street_number']},
                                        {'long_name': 'Hacker Way', 'short_name': 'Hacker Way', 'types': ['route']},
                                        {'long_name': 'Menlo Park', 'short_name': 'Menlo Park',
                                         'types': ['locality', 'political']},
                                        {'long_name': 'San Mateo County', 'short_name': 'San Mateo County',
                                         'types': ['administrative_area_level_2', 'political']},
                                        {'long_name': 'California', 'short_name': 'CA',
                                         'types': ['administrative_area_level_1', 'political']},
                                        {'long_name': 'United States', 'short_name': 'US',
                                         'types': ['country', 'political']},
                                        {'long_name': '94025', 'short_name': '94025', 'types': ['postal_code']}],
                 'formatted_address': '10 Hacker Way, Menlo Park, CA 94025, USA',
                 'geometry': {'location': {'lat': 37.4835791, 'lng': -122.1500939}, 'location_type': 'ROOFTOP',
                              'viewport': {'northeast': {'lat': 37.4849280802915, 'lng': -122.1487449197085},
                                           'southwest': {'lat': 37.4822301197085, 'lng': -122.1514428802915}}},
                 'place_id': 'ChIJ_wMBpJe8j4ARVIR-F8nC79c',
                 'plus_code': {'compound_code': 'FRMX+CX Menlo Park, CA, USA', 'global_code': '849VFRMX+CX'},
                 'types': ['establishment', 'point_of_interest']}, {
                    'address_components': [{'long_name': '1101', 'short_name': '1101', 'types': ['street_number']},
                                           {'long_name': 'Dexter Avenue North', 'short_name': 'Dexter Ave N',
                                            'types': ['route']}, {'long_name': 'Westlake', 'short_name': 'Westlake',
                                                                  'types': ['neighborhood', 'political']},
                                           {'long_name': 'Seattle', 'short_name': 'Seattle',
                                            'types': ['locality', 'political']},
                                           {'long_name': 'King County', 'short_name': 'King County',
                                            'types': ['administrative_area_level_2', 'political']},
                                           {'long_name': 'Washington', 'short_name': 'WA',
                                            'types': ['administrative_area_level_1', 'political']},
                                           {'long_name': 'United States', 'short_name': 'US',
                                            'types': ['country', 'political']},
                                           {'long_name': '98109', 'short_name': '98109', 'types': ['postal_code']}],
                    'formatted_address': '1101 Dexter Ave N, Seattle, WA 98109, USA',
                    'geometry': {'location': {'lat': 47.6288591, 'lng': -122.3427307}, 'location_type': 'ROOFTOP',
                                 'viewport': {'northeast': {'lat': 47.6302080802915, 'lng': -122.3413817197085},
                                              'southwest': {'lat': 47.6275101197085, 'lng': -122.3440796802915}}},
                    'place_id': 'ChIJidZEkT4VkFQR9ICo-0-86QY',
                    'plus_code': {'compound_code': 'JMH4+GW Seattle, WA, USA', 'global_code': '84VVJMH4+GW'},
                    'types': ['establishment', 'point_of_interest']}], 'status': 'OK'

}

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


class MockResponseGeo:
    def json(self):
        return GEOCODING_DATA


class MockResponsePage:
    def json(self):
        return WIKI_DATA_PAGE


class MockResponseDescription:
    def json(self):
        return WIKI_DATA_DESC

@mock.patch.dict(os.environ, {'GOOGLEKEY': "Fake_key"})
class TestView(unittest.TestCase):
    """
    This class test the views.
    """

    def setUp(self):
        self.url_wiki = "https://fr.wikipedia.org/w/api.php"
        self.lat = 37.4835791
        self.lng = -122.1500939
        self.parsed_input = "facebook"
        self.input = "Donne moi l'adresse de Facebook"
        self.url_geo = "https://maps.googleapis.com/maps/api/geocode/json?"
        self.address = "10 Hacker Way, Menlo Park, CA 94025, USA"
        self.message = "Quelle aventure! Je te raconte mon petit:"
        self.end_message = "T'aimes mes histoires?"
        self.mess_wiki = "Facebook City ou Zee-Town (Ville Facebook, ou Ville Z, comme Zuckerberg) est un important"
        " projet de création de ville nouvelle-campus urbanisé-cité idéale d'environ 80 hectares. "
        "Ce projet est lancé en 2012 par Mark Zuckerberg, PDG fondateur de la société américaine de réseautage social " \
        "Facebook (entreprise), "
        " à Menlo Park, dans la baie de San Francisco, de la Silicon Valley, en Californie, aux États-Unis,."

    def test_index(self):
        """
        Check if the status of response is ok.
        """
        with app.test_client() as c:
            response = c.get('/')
            self.assertEqual(response.status_code, 200)

    def test_parser(self):
        p = Parser(self.input)
        results = p.transform_input()
        self.assertEqual(results, self.parsed_input)

    def test_geocoding_send_request(self):
        params = {
            "key": "Fake_key",
            "address": self.parsed_input
        }

        with patch('app.api.geocoding.requests.get') as mock_requests:
            geo = Geocoding(self.parsed_input)
            mock_requests.return_value = MockResponseGeo()
            results = geo.send_request()
            self.assertEqual(results, GEOCODING_DATA)
            mock_requests.assert_called_once_with(self.url_geo, params=params)

    def test_wiki_get_page(self):
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
            mock_requests.assert_called_once_with(self.url_wiki, params=params)

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
            mock_requests.return_value = MockResponseDescription()
            wiki.page = WIKI_DATA_PAGE["query"]["geosearch"][0]['pageid']
            results = wiki.get_description()
            self.assertEqual(results, WIKI_DATA_DESC["query"]["pages"][str(wiki.page)]["extract"])
            mock_requests.assert_called_once_with(self.url_wiki, params=params)

    def test_process(self):
        with app.test_client() as c:
            rv = c.post('/process', json={'input_user': self.parsed_input, 'lat': self.lat, 'lng': self.lng,
                                          'address': self.address, "message": self.message,
                                          'end_mess': self.end_message, 'wiki': self.mess_wiki})
            self.assertEqual(rv.status_code, 200)
