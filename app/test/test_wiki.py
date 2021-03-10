import pytest
import urllib.request
from app.api.wiki import Wiki


class TestWiki:
    """
    Class test for the Wikipedia class.
    """
    def test_request_page(self, monkeypatch):
        wiki = Wiki(37.4835791, -122.1500939)
        data_page = {'batchcomplete': '', 'query': {'geosearch': [{'pageid': 10142861, 'ns': 0, 'title': 'Facebook City', 'lat': 37.481027, 'lon': -122.153898, 'dist': 439.5, 'primary': ''}]}}

        def mockreturn():
            return data_page

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert wiki.get_page() == data_page["query"]["geosearch"][0]['pageid']

    def test_request_description(self, monkeypatch):
        wiki = Wiki(37.4835791, -122.1500939)
        data_description = {'batchcomplete': '', 'query': {'pages': {'10142861': {'pageid': 10142861, 'ns': 0, 'title': 'Facebook City', 'extract': "Facebook City ou Zee-Town (Ville Facebook, ou Ville Z, comme Zuckerberg) est un important projet de création de ville nouvelle-campus urbanisé-cité idéale d'environ 80 hectares. Ce projet est lancé en 2012 par Mark Zuckerberg, PDG fondateur de la société américaine de réseautage social Facebook (entreprise), à Menlo Park, dans la baie de San Francisco, de la Silicon Valley, en Californie, aux États-Unis,."}}}}

        def mockreturn():
            return data_description

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert wiki.get_description() == data_description["query"]["pages"]["10142861"]["extract"]


