import unittest

from app.message import get_message, get_end_message, get_errors_response
from app.config import MESSAGE_LIST, END_LIST, ERROR_DICT


class TestMessage(unittest.TestCase):
    """
    Class test for the functions messages.
    """

    def setUp(self):
        """
        Unittest setup
        """
        self.message = get_message()
        self.end_message = get_end_message()
        self.error_message = get_errors_response("no_found_mess")

    def test_get_message(self):
        """
        Check if the message is in the message list
        """
        messages = MESSAGE_LIST
        self.assertIn(self.message, messages)

    def test_get_end_message(self):
        """
        Check if the message is in the end message list.
        """
        ends = END_LIST
        if self.end_message in ends:
            self.assertIsNotNone(self.end_message)

    def test_get_error_message(self):
        """
        Check if the message is in the error message list.
        """
        errors = ERROR_DICT
        if self.error_message in errors:
            self.assertListEqual(self.error_message, errors["no_found_mess"])
