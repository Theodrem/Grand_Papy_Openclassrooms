import requests
import os

from app.message import get_errors_response


class Geocoding:
    def __init__(self, adress):
        self.key = os.environ['GOOGLEKEY']
        self.address = adress
        self.current = None
        self.geo_mess = "no_found_geocoding"
        self.send_request()

    def send_request(self):
        params = {
            "key": self.key,
            "address": self.address
        }

        base_url = "https://maps.googleapis.com/maps/api/geocode/json?"
        try:
            response = requests.get(base_url, params=params)
            self.current = response.json()
            return self.current
        except requests.exceptions.ConnectionError:
            return get_errors_response("no_found_geocoding")

    def get_latitude(self):
        try:
            return self.current['results'][0]['location']['lat']
        except KeyError:
            return self.current['results'][0]['geometry']['location']['lat']
        except TypeError:
            return get_errors_response("no_found_geocoding")

    def get_longitude(self):
        try:
            return self.current['results'][0]['location']['lng']
        except KeyError:
            return self.current['results'][0]['geometry']['location']['lng']
        except TypeError:
            return get_errors_response("no_found_geocoding")

    def get_address(self):
        try:
            return self.current['results'][0]['formatted_address']
        except TypeError:
            return get_errors_response("no_found_geocoding")



