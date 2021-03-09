import unittest
from unittest.mock import patch

from app.api.geocoding import Geocoding


class TestGeocoding(unittest.TestCase):
    def setUp(self):
        self.expected_geo_name = "paris"
        self.geo = Geocoding(self.expected_geo_name)
        self.expected = {'results':
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
        self.expected_lat = self.expected['results'][0]['geometry']['location']['lat']
        self.expected_lng = self.expected['results'][0]['geometry']['location']['lat']
        self.expected_address = self.expected['results'][0]['formatted_address']

    @patch.object(Geocoding, 'send_request')
    def test_send_request(self, mock_send_request):
        mock_send_request.return_value = self.expected
        result = self.geo.send_request()
        self.assertEqual(self.expected, result)

    @patch.object(Geocoding, 'get_latitude')
    def test_get_latitude(self, mock_get_latitude):
        mock_get_latitude.return_value = self.expected_lat
        result = self.geo.get_latitude()
        self.assertEqual(self.expected_lat, result)

    @patch.object(Geocoding, 'get_longitude')
    def test_get_latitude(self, mock_get_longitude):
        mock_get_longitude.return_value = self.expected_lng
        result = self.geo.get_longitude()
        self.assertEqual(self.expected_lng, result)

    @patch.object(Geocoding, 'get_address')
    def test_get_latitude(self, mock_get_address):
        mock_get_address.return_value = self.expected_address
        result = self.geo.get_address()
        self.assertEqual(self.expected_address, result)






