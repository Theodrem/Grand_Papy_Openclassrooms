import unittest
from unittest.mock import patch
from app.api.geocoding import Geocoding
import mock
import os


GEOCODING_DATA = {'results':
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


class MockResponse:
    def json(self):
        return GEOCODING_DATA


@mock.patch.dict(os.environ, {'GOOGLEKEY': "Fake_key"})
class TestGeocoding(unittest.TestCase):

    def setUp(self):
        self.address = "paris"
        self.url = "https://maps.googleapis.com/maps/api/geocode/json?"

        self.params = {
            "key": "Fake_key",
            "address": self.address
        }

    def test_send_request(self):
        with patch('app.api.geocoding.requests.get') as mock_requests:
            geo = Geocoding(self.address)
            mock_requests.return_value = MockResponse()
            results = geo.send_request()
            self.assertEqual(results, GEOCODING_DATA)
            mock_requests.assert_called_once_with(self.url, params=self.params)

    def test_get_latitude(self):
        geo = Geocoding(self.address)
        geo.current = GEOCODING_DATA
        results = geo.get_latitude()
        self.assertEqual(results, GEOCODING_DATA['results'][0]['geometry']['location']['lat'])

    def test_get_lng(self):
        geo = Geocoding(self.address)
        geo.current = GEOCODING_DATA
        results = geo.get_longitude()
        self.assertEqual(results, GEOCODING_DATA['results'][0]['geometry']['location']['lng'])

    def test_get_address(self):
        geo = Geocoding(self.address)
        geo.current = GEOCODING_DATA
        results = geo.get_address()
        self.assertEqual(results, GEOCODING_DATA['results'][0]['formatted_address'])
