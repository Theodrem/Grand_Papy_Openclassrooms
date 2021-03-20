import unittest
from mock import mock
from app.api.geocoding import Geocoding
from app.api.wiki import Wiki
from app.parser import Parser
from app.message import get_message, get_end_message
from app.config import END_LIST, MESSAGE_LIST
from app import app

GEOCODING_DATA = {'results': [{'address_components': [{'long_name': '10', 'short_name': '10', 'types': ['street_number']},
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
                  'types': ['establishment', 'point_of_interest']}], 'status': 'OK'}


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

    def test_index(self):
        """
        Check if the status of response is ok.
        """
        with app.test_client() as c:
            response = c.get('/')
            self.assertEqual(response.status_code, 200)

    @mock.patch("app.api.wiki.Wiki")
    @mock.patch("app.api.geocoding.Geocoding")
    def test_process(self, mock_geo, mock_wiki):
        """
        Check if the process view with the post method is correct
        """

        mock_geo.return_value.send_request.return_value = GEOCODING_DATA
        geo = mock_geo(self.parsed_input)
        self.assertEqual(geo.send_request(), GEOCODING_DATA)

        mock_wiki.return_value.get_page.return_value = WIKI_DATA_PAGE
        wiki = mock_wiki(self.lat, self.lng)
        self.assertEqual(wiki.get_page(), WIKI_DATA_PAGE)

        p = Parser(self.input)

        end_message = get_end_message()
        message = get_message()

        with app.test_client() as c:
            rv = c.post('/process', json={'input_user': p.transform_input(), 'lat': self.lat, 'lng': self.lng,
                    'address': self.address, "message": message,
                    'end_mess': end_message, 'wiki':  WIKI_DATA_DESC["query"]["pages"][str(10142861)]["extract"]})

            self.assertEqual(rv.status_code, 200)

            mock_geo.return_value.get_latitude.return_value = self.lat
            self.assertEqual(geo.get_latitude(), self.lat)

            mock_geo.return_value.get_longitude.return_value = self.lng
            self.assertEqual(geo.get_longitude(), self.lng)

            mock_geo.return_value.get_address.return_value = self.address
            self.assertEqual(geo.get_address(), self.address)

            mock_wiki.return_value.get_description.return_value = WIKI_DATA_DESC["query"]["pages"][str(10142861)]["extract"]
            self.assertEqual(wiki.get_description(), WIKI_DATA_DESC["query"]["pages"][str(10142861)]["extract"])

            self.assertEqual(p.transform_input(), self.parsed_input)

            self.assertIn(end_message, END_LIST)
            self.assertIn(message, MESSAGE_LIST)
