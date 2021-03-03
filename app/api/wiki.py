import requests

from app.message import get_errors_response


class Wiki:
    def __init__(self, lat, lng):
        self.lat = lat  # Latitude place
        self.lng = lng  # Longitude place
        self.page = None
        self.wiki_mess = "no_found_wiki"  # Error dictionary key

    def get_page(self):
        """
        :return: The page id
        """
        parameters = {  # request parameters
            "action": "query",
            "list": "geosearch",
            "gsradius": 1000,
            "gscoord": "%s|%s" % (self.lat, self.lng),
            "format": "json",
        }
        try:
            """
            Try send request. If there is an error in connexion return error message.
            """
            response = requests.get("https://fr.wikipedia.org/w/api.php", params=parameters)
            data = response.json()
        except requests.exceptions.ConnectionError:
            return get_errors_response(self.wiki_mess)

        try:
            """
            Try get pageid data. If there is a key error return error message.
            """
            page = data["query"]["geosearch"][0]['pageid']
            self.page = page
            return self.page
        except KeyError:
            return get_errors_response("no_found_wiki")

    def get_description(self):
        """
        :return: Place description of Mediawiki
        """
        self.get_page()
        parameters = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "exintro": "1",
            "explaintext": "1",
            "exsentences": "5",
            "pageids": self.page
        }
        try:
            """
            Try send request. If there is an error in connexion return error message.
            """
            response = requests.get("https://fr.wikipedia.org/w/api.php", params=parameters)
            data = response.json()
        except requests.exceptions.ConnectionError:
            return get_errors_response("no_found_wiki")

        try:
            """
            Try get extract data. If there is a key error return error message.
            """
            description_wiki = data["query"]["pages"][str(self.page)]["extract"]
            return description_wiki
        except KeyError:
            return get_errors_response("no_found_wiki")


