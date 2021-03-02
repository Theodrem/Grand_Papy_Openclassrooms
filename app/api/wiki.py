import requests

from app.message import get_errors_response


class Wiki:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng
        self.page = None
        self.wiki_mess = "no_found_wiki"

    def get_page(self):
        parameters = {
            "action": "query",
            "list": "geosearch",
            "gsradius": 1000,
            "gscoord": "%s|%s" % (self.lat, self.lng),
            "format": "json",
        }
        response = requests.get("https://fr.wikipedia.org/w/api.php", params=parameters)
        data = response.json()

        try:
            page = data["query"]["geosearch"][0]['pageid']
            self.page = page
            return self.page
        except KeyError:
            return get_errors_response("no_found_wiki")

    def get_description(self):
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

        response = requests.get("https://fr.wikipedia.org/w/api.php", params=parameters)
        data = response.json()
        try:
            description_wiki = data["query"]["pages"][str(self.page)]["extract"]
            return description_wiki
        except KeyError:
            get_errors_response("no_found_wiki")


