import unittest
from app.config import STOP_WORDS
from app.parser import Parser


class TestParser(unittest.TestCase):
    def setUp(self):
        self.list_stop_words = STOP_WORDS
        self.parse = Parser("Salut papi adresse Openclassrooms")
        self.parse2 = Parser("Dis moi l'adresse de facebook")

    def test_transform_input(self):
        list_verify = []
        parsing = self.parse.transform_input()

        for word in self.list_stop_words:
            if word in parsing.split(' '):
                list_verify.append(word)

        self.assertEqual(list_verify, [])

    def test_transform_two(self):
        self.assertEqual(self.parse2.transform_input(), "facebook")
