import unittest

from app import app
from app.parser import Parser
from app.message import get_message, get_end_message, get_errors_response
from app.config import END_LIST, MESSAGE_LIST, ERROR_DICT


class TestView(unittest.TestCase):
    """
    This class test the views.
    """

    def setUp(self):
        self.user_input = "Dis moi l'adresse de facebook"
        self.result_geocoding = {'results':
                                 [{'formatted_address': '10 Hacker Way, Menlo Park, CA 94025, USA',
                                   'geometry':
                                   {'location':
                                    {'lat': 37.4835791, 'lng': -122.1500939}
                                    }}]}

        self.result_wiki = {'query':
                            {'pages':
                             {'10142861':
                              {'extract': "Facebook City ou Zee-Town (Ville Facebook, ou Ville Z, comme "
                               "Zuckerberg) est un important projet de création de ville "
                               "nouvelle-campus urbanisé-cité idéale d'environ 80 hectares. Ce "
                               "projet est lancé en 2012 par Mark Zuckerberg, PDG fondateur de "
                               "la société américaine de réseautage social Facebook ("
                               "entreprise), à Menlo Park, dans la baie de San Francisco, "
                               "de la Silicon Valley, en Californie, aux États-Unis,."}

                              }}}

    def test_index(self):
        """
        Check if the status of response is ok.
        """
        with app.test_client() as c:
            response = c.get('/')
            self.assertEquals(response.status_code, 200)

    def test_sentense(self):
        """
        Check if the parser class return the correct values.
        """
        sentence = Parser(self.user_input)
        parsed_input = sentence.transform_input()
        self.assertEqual(parsed_input, "facebook")

    def test_lng(self):
        """
        Check if the Geocoding class return the correct latitude.
        """
        lng = self.result_geocoding['results'][0]['geometry']['location']['lng']
        self.assertEqual(lng, -122.1500939)

    def test_lat(self):
        """
        Check if the Geocoding class return the correct longitude.
        """
        lat = self.result_geocoding['results'][0]['geometry']['location']['lat']
        self.assertEqual(lat, 37.4835791)

    def test_address(self):
        """
        Check if the Geocoding class return the correct address.
        """
        address = self.result_geocoding['results'][0]['formatted_address']
        self.assertEqual(address, '10 Hacker Way, Menlo Park, CA 94025, USA')

    def test_message_wiki(self):
        """
        Check part of the description to see if it is correct.
        """
        mess_wiki = self.result_wiki['query']['pages']['10142861']['extract']
        self.assertIn("Facebook City ou Zee-Town", mess_wiki)

    def test_message(self):
        """
        Check if the message is in the message list.
        """
        message = get_message()
        self.assertIn(message, MESSAGE_LIST)

    def test_end_message(self):
        """
        Check if the message is in the end message list.
        """
        end_message = get_end_message()
        self.assertIn(end_message, END_LIST)

    def test_error_message(self):
        """
        Check if the message is in the error message list.
        """
        mess_wiki = get_errors_response("no_found_wiki")
        self.assertEqual(mess_wiki, ERROR_DICT["no_found_wiki"])

    def test_error_message_no_found(self):
        """
        Check if the message is correct.
        """
        message = get_errors_response("no_found_mess")
        self.assertEqual(message, ERROR_DICT["no_found_mess"])
