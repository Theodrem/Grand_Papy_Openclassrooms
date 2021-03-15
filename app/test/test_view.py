from mock import patch
from app.api.geocoding import Geocoding
from app.api.wiki import Wiki
from app import app


class TestView:
    """
    This class test the views.
    """

    def test_index(self):
        """
        Check if the status of response is ok.
        """
        with app.test_client() as c:
            response = c.get('/')
            assert response.status_code == 200

    def test_process(self):
        parsed_input = "facebook"
        lng = -122.1500939
        lat = 37.4835791
        address = "10 Hacker Way, Menlo Park, CA 94025, USA"
        message = "Quelle aventure! Je te raconte mon petit:"
        end_message = "T'aimes mes histoires?"
        mess_wiki = "Facebook City ou Zee-Town (Ville Facebook, ou Ville Z, comme Zuckerberg) est un important"
        " projet de création de ville nouvelle-campus urbanisé-cité idéale d'environ 80 hectares. "
        "Ce projet est lancé en 2012 par Mark Zuckerberg, PDG fondateur de la société américaine de réseautage social " \
        "Facebook (entreprise), "
        " à Menlo Park, dans la baie de San Francisco, de la Silicon Valley, en Californie, aux États-Unis,."

        @patch('Geocoding.send_request')
        def mock_geocoding(mock_geocoding):
            geo = Geocoding(parsed_input)
            mock_geocoding.return_value = lat
            result_lat = geo.get_latitude()
            assert result_lat == mock_geocoding

            mock_geocoding.return_value = lng
            result_lng = geo.get_longitude()
            assert result_lng == mock_geocoding

        @patch('Wiki.get_description')
        def mock_geocoding(mock_wiki):
            wiki = Wiki(lat, lng)
            mock_geocoding.return_value = mess_wiki
            result_page = wiki.get_description()
            assert result_page == mock_wiki

        with app.test_client() as c:
            rv = c.post('/process', json={'input_user': parsed_input, 'lat': lat, 'lng': lng,
                                          'address': address, "message": message,
                                          'end_mess': end_message, 'wiki': mess_wiki})
            assert rv.status_code == 200


