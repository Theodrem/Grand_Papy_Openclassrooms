import unittest

from app.message import get_message, get_end_message, get_errors_response
from app.config import ANSWER_LIST, END_LIST, ERROR_DICT


class TestMessage(unittest.TestCase):
    def setUp(self):
        self.message = get_message()
        self.end_message = get_end_message()
        self.error_message = get_errors_response("no_found_mess")

    def test_get_message(self):
        answers = ANSWER_LIST
        if self.message in answers:
            self.assertIsNotNone(self.message)

    def test_get_end_message(self):
        ends = END_LIST
        if self.end_message in ends:
            self.assertIsNotNone(self.end_message)

    def test_get_error_message(self):
        errors = ERROR_DICT
        if self.error_message in errors:
            self.assertListEqual(self.error_message, errors["no_found_mess"])
