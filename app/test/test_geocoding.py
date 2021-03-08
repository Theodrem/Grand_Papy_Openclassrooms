import unittest
from unittest.mock import Mock

from app.api.geocoding import Geocoding
from app.message import get_errors_response


class TestGeocoding(unittest.TestCase):
    def setUp(self):
        self.geo = Geocoding("paris")
        self.get_errors_response = get_errors_response
        self.geo.send_request = Mock()
        self.response = {'results':
            [{'address_components': [
                {'long_name': 'Paris', 'short_name': 'Paris', 'types': ['locality', 'political']},
                {'long_name': 'Paris', 'short_name': 'Paris',
                 'types': ['administrative_area_level_2', 'political']},
                {'long_name': 'Île-de-France', 'short_name': 'IDF',
                 'types': ['administrative_area_level_1', 'political']},
                {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}],
                'formatted_address': 'Paris, France', 'geometry': {
                    'bounds': {'northeast': {'lat': 48.9021449, 'lng': 2.4699208},
                               'southwest': {'lat': 48.815573, 'lng': 2.224199}},
                    'location': {'lat': 48.856614, 'lng': 2.3522219},
                    'location_type': 'APPROXIMATE',
                    'viewport': {'northeast': {'lat': 48.9021449, 'lng': 2.4699208},
                                 'southwest': {'lat': 48.815573, 'lng': 2.224199}}},
                'place_id': 'ChIJD7fiBh9u5kcRYJSMaMOCCwQ', 'types': ['locality', 'political']}],
            'status': 'OK'}

    def test_send_request(self):
        self.assertEqual(self.geo.current, self.response)

    def test_get_latitude(self):
        try:
            self.assertEqual(self.geo.current['results'][0]['location']['lat'], 48.856614)
        except KeyError:
            self.assertEqual(self.geo.current['results'][0]['geometry']['location']['lat'], 48.856614)

    def test_get_longitude(self):
        try:
            self.assertEqual(self.geo.current['results'][0]['location']['lng'], 2.3522219)
        except KeyError:
            self.assertEqual(self.geo.current['results'][0]['geometry']['location']['lng'], 2.3522219)

    def test_get_address(self):
        try:
            self.assertEqual(self.geo.current['results'][0]['formatted_address'], 'Paris, France')
        except TypeError:
            self.assertEqual(self.get_errors_response("no_found_geocoding"), get_errors_response("no_found_geocoding"))


