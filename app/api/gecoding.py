from boto.s3.connection import S3Connection
import requests
import os

from app.message import get_errors_response


class Geocoding:
    """
    This class queries the geocoding API.
    Get latitude, longitude and address for Google maps api.
    """

    def __init__(self, place):
        try:
            self.key = S3Connection(os.environ['GOOGLEKEY'])
        except KeyError:
            self.key = ""

        self.place = place
        self.current = None
        self.geo_mess = "no_found_geocoding"  # Error dictionary key
        self.send_request()

    def send_request(self):
        """
        :return: Data request
        """
        params = {
            "key": self.key,
            "address": self.place
        }

        base_url = "https://maps.googleapis.com/maps/api/geocode/json?"

        try:
            """
            Try send request. If there is an error in connexion return error message
            """
            response = requests.get(base_url, params=params)
            self.current = response.json()
            return self.current
        except requests.exceptions.ConnectionError:
            return get_errors_response("no_found_geocoding")

    def get_latitude(self):
        """
        :return: Latitude place
        """
        try:
            """
            Try get latitude. If there is a key error or type error return error message.
            """
            return self.current['results'][0]['location']['lat']
        except KeyError:
            return self.current['results'][0]['geometry']['location']['lat']
        except TypeError:
            return get_errors_response("no_found_geocoding")

    def get_longitude(self):
        """
        :return: Longitude place
        """
        try:
            """
            Try get longitude. If there is a key error or type error return error message.
            """
            return self.current['results'][0]['location']['lng']
        except KeyError:
            return self.current['results'][0]['geometry']['location']['lng']
        except TypeError:
            return get_errors_response("no_found_geocoding")

    def get_address(self):
        """
        Try get address. If there is a type error return error message.
        :return: Address plac
        """

        try:
            return self.current['results'][0]['formatted_address']
        except TypeError:
            return get_errors_response("no_found_geocoding")
