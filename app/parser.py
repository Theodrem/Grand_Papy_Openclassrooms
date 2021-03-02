from app.config import STOP_WORDS


class Parser:
    def __init__(self, input_user):
        self.input = input_user

    def transform_input(self):
        list_stopwords = STOP_WORDS
        self.input = self.input.lower()
        self.input = self.input.split()
        self.input = [word for word in self.input if word not in list_stopwords]
        self.input = " ".join(self.input)
        return self.input



