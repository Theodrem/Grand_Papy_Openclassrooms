import unittest


class TestGeocoding(unittest.TestCase):
    """
    Class test for the Geocoding class.
    """

    def setUp(self):
        """
        Unittest setup
        """
        self.place = "tokyo"
        self.place_2 = "tour pise"

        self.current = {'results': [{'formatted_address':
                                     'Tokyo, Japan',
                                     'location': {'lat': 35.6761919, 'lng': 139.6503106}
                                     }]}

        self.current_2 = {'results': [{'formatted_address':
                                       'Piazza del Duomo, 56126 Pisa PI, Italy',
                                       'geometry':
                                       {'location': {'lat': 43.722952, 'lng': 10.396597}
                                        }}]}

    def test_send_request(self):
        """
        :return: Data to false request number one.
        """
        if self.current is list:
            return self.current

    def test_send_request_2(self):
        """
        :return:  Data to false request number two.
        """
        if self.current_2 is list:
            return self.current_2

    def test_get_latitude(self):
        """
        Check if the latitude number one is correct
        """
        get_lat = self.current['results'][0]['location']['lat']
        self.assertEqual(get_lat, 35.6761919)

    def test_get_longitude(self):
        """
        Check if the longitude number one is correct
        """
        get_lng = self.current['results'][0]['location']['lng']
        self.assertEqual(get_lng, 139.6503106)

    def test_get_latitude_2(self):
        """
        Check if the latitude number two is correct
        """
        get_lat = self.current_2['results'][0]['geometry']['location']['lat']
        self.assertEqual(get_lat, 43.722952)

    def test_get_longitude_2(self):
        """
        Check if the longitude number two is correct
        """
        get_lng = self.current_2['results'][0]['geometry']['location']['lng']
        self.assertEqual(get_lng, 10.396597)
