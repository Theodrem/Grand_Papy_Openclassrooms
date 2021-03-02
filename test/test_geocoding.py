import unittest


class TestGeocoding(unittest.TestCase):
    def setUp(self):
        self.place = "tokyo"
        self.place_2 = "tour pise"

        self.current = {'results': [{'formatted_address':
                            'Tokyo, Japan',
                        'location': {'lat': 35.6761919, 'lng': 139.6503106}
                        }]}

        self.current_2 = {'results':[{'formatted_address':
                              'Piazza del Duomo, 56126 Pisa PI, Italy',
                          'geometry':
                              {'location': {'lat': 43.722952, 'lng': 10.396597}
                               }}]}

    def test_send_request(self):
        if self.current is list:
            return self.current

    def test_send_request_2(self):
        if self.current_2 is list:
            return self.current_2

    def test_get_latitude(self):
        get_lat = self.current['results'][0]['location']['lat']
        self.assertEqual(get_lat, 35.6761919)

    def test_get_longitude(self):
        get_lng = self.current['results'][0]['location']['lng']
        self.assertEqual(get_lng, 139.6503106)

    def test_get_latitude_2(self):
        get_lat = self.current_2['results'][0]['geometry']['location']['lat']
        self.assertEqual(get_lat, 43.722952)

    def test_get_longitude_2(self):
        get_lng = self.current_2['results'][0]['geometry']['location']['lng']
        self.assertEqual(get_lng, 10.396597)