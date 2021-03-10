import pytest
import urllib.request
from app.api.geocoding import Geocoding


class TestGeocoding:

    def test_request(self, monkeypatch):
        geo = Geocoding("paris")
        data = {'results':
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

        data_lat = data['results'][0]['geometry']['location']['lat']
        data_lng = data['results'][0]['geometry']['location']['lng']
        data_address = data['results'][0]['formatted_address']

        def mockreturn():
            return data

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert geo.send_request() == data
        assert geo.get_latitude() == data_lat
        assert geo.get_longitude() == data_lng
        assert geo.get_address() == data_address
