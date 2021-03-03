import random

from app.config import MESSAGE_LIST, END_LIST, ERROR_DICT


def get_message():
    """
    :return: The random message in ANSWER_LIST
    """
    message = random.choice(MESSAGE_LIST)
    return message


def get_end_message():
    """
    :return: The random message in END_LIST
    """
    end = random.choice(END_LIST)
    return end


def get_errors_response(name):
    """
    :return: The message from ERROR_DICT with the key in parameter
    """
    return ERROR_DICT[name]
