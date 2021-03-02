import random

from app.config import ANSWER_LIST, END_LIST, ERROR_DICT


def get_message():
    message = random.choice(ANSWER_LIST)
    return message


def get_end_message():
    end = random.choice(END_LIST)
    return end


def get_errors_response(name):
    return ERROR_DICT[name]
