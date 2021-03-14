import unittest
from unittest.mock import patch
from app.config import STOP_WORDS
from app.parser import Parser


class TestParser(unittest.TestCase):
    """
    This class test the Parser class.
    """
    def setUp(self):
        self.value_two = "tour pise"

    def test_transform_input(self):
        """
        Parse the input
        Check if there are bad words in the parsed entry.
        """
        parse = Parser("Dis moi l'adresse de facebook")
        results = parse.transform_input()
        self.assertEqual(len([word for word in results.split(" ") if word not in STOP_WORDS]), 1)

    def test_transform_two(self):
        """
        Check if the parsed input is good.
        """
        with patch('app.parser.Parser') as mock_text:
            parse_two = Parser("Salut papy donne moi l'adresse de la tour de pise")
            mock_text.return_value = self.value_two
            results = parse_two.transform_input()
            self.assertEqual(parse_two.transform_input(), self.value_two)
