import unittest


from app import app


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
