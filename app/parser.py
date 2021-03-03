from app.config import STOP_WORDS


class Parser:
    """
    the utility of this class is parsing the user input
    """
    def __init__(self, input_user):
        self.input = input_user

    def transform_input(self):
        """
        :return: Parsed user input
        """
        list_stopwords = STOP_WORDS
        self.input = self.input.lower()  # lowercase all letters
        self.input = self.input.split()  # Transform string to list
        self.input = [word for word in self.input if word not in list_stopwords]  # Checks if a word of the input is
        # in the stop_words list
        self.input = " ".join(self.input) # Transform the rest of the list into a string
        return self.input



