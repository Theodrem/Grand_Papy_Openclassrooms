from app.config import STOP_WORDS
from app.parser import Parser


class TestParser:
    """
    This class test the Parser class.
    """
    def test_transform_input(self):
        """
        Parse the input
        Check if there are bad words in the parsed entry.
        """
        parse = Parser("Dis moi l'adresse de facebook")
        parsing = parse.transform_input()
        assert len([word for word in parsing.split(" ") if word not in STOP_WORDS]) == 1

    def test_transform_two(self):
        """
        Check if the parsed input is good.
        """
        parse_two = Parser("Salut papy donne moi l'adresse de la tour de pise")
        assert parse_two.transform_input() == "tour pise"
