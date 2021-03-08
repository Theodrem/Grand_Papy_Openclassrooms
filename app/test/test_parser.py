import unittest

from app.config import STOP_WORDS
from app.parser import Parser


class TestParser(unittest.TestCase):
    """
    This class test the Parser class.
    """

    def setUp(self):
        """
        Unittest setup
        """
        self.list_stop_words = STOP_WORDS
        self.parse = Parser("Salut papi adresse Openclassrooms")
        self.parse2 = Parser("Dis moi l'adresse de facebook")

    def test_transform_input(self):
        """
        Parse the input
        Check if there are bad words in the parsed entry.
        """
        parsing = self.parse.transform_input()
        self.assertEqual(len([word for word in parsing.split(" ") if word not in self.list_stop_words]), 0)

    def test_transform_two(self):
        """
        Check if the parsed input is good.
        """
        self.assertEqual(self.parse2.transform_input(), "facebook")
