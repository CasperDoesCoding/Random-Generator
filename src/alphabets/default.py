"""
    This contains the default alphabet parent
    class which is used by the generators by default.
    The default alphabet is american english.
"""

from random import randint


class Alphabet:
    """
    This is the parent class for all alphabets.
    """

    name = "American English"
    letters = "abcdefghijklmnopqrstuvwxyz"
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    def __init__(self) -> None:
        self.letters_both_cases = self.letters + self.get_uppercase()

    def get_random_punctuation(self):
        """
        This function returns a random punctuation mark.
        """
        return self.punctuation[randint(0, len(self.punctuation) - 1)]

    def get_random_letter(self, letter_style: str = "random"):
        """
        This function returns a random

        :param letter_style: The style of the letter.
        Can be "random", "uppercase" or "lowercase".
        """
        if letter_style == "random":
            return self.letters_both_cases[randint(0, len(self.letters_both_cases) - 1)]
        elif letter_style == "uppercase":
            return self.get_uppercase()[randint(0, len(self) - 1)]
        elif letter_style == "lowercase":
            return self.get_lowercase()[randint(0, len(self) - 1)]

    def get_letter_by_index(self, index: int):
        """
        This function returns a letter from the alphabet.
        """
        return self.letters[index]

    def get_letter_by_index_both_cases(self, index: int):
        """
        This function returns a letter from the alphabet in both cases.
        """
        return self.letters_both_cases[index]

    def get_punctuation_by_index(self, index: int):
        """
        This function returns the punctuation marks.
        """
        return self.punctuation[index]

    def get_punctuation(self):
        """
        This function returns the punctuation marks.
        """
        return self.punctuation

    def get_uppercase(self):
        """
        This function returns the alphabet in upper case.
        """
        return str.upper(self.letters)

    def get_lowercase(self):
        """
        This function returns the alphabet in lower case.
        """
        return str.lower(self.letters)

    def get_both_cases(self):
        """
        This function returns the alphabet in both cases.
        """
        return self.letters_both_cases

    def get_name(self):
        """
        This function returns the name of the alphabet.
        """
        return self.name

    def __len__(self):
        return len(self.letters)

    def __str__(self):
        return self.letters

    def __repr__(self):
        return f"{self.name} > {self.letters_both_cases}"
