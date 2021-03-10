from app.message import get_message, get_end_message, get_errors_response
from app.config import MESSAGE_LIST, END_LIST, ERROR_DICT


class TestMessage:
    """
    Class test for the functions messages.
    """

    def test_get_message(self):
        """
        Check if the message is in the message list
        """
        message = get_message()
        messages = MESSAGE_LIST
        assert message in messages

    def test_get_end_message(self):
        """
        Check if the message is in the end message list.
        """
        end_message = get_end_message()
        end_messages = END_LIST

        assert end_message in end_messages

    def test_get_error_message(self):
        """
        Check if the message is in the error message list.
        """
        errors = ERROR_DICT
        error = get_errors_response("no_found_wiki")

        assert error in errors.values()

