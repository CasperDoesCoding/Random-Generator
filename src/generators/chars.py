"""
    This generator generates things related to characters.
    such as utf-8 characters, random characters, etc.

    Author: github.com/CasperDoesCode
"""

from enum import Enum
from random import randint
from alphabets.default import Alphabet


class OutputMode(Enum):
    """
    Enum for the different output modes.

    - NORMAL: No restrictions on the output.
    - VALID_INTERNET_USAGE: Output that is valid for internet usage
    - VALID_FILE_NAME: Output that is valid for file names
    """

    NORMAL = 0
    VALID_INTERNET_USAGE = 1
    VALID_FILE_NAME = 2


class Chars:
    """
    This class generates random char related stuff.
    """

    def __init__(
        self,
        output_mode: OutputMode = OutputMode.NORMAL,
        alphabet: Alphabet = Alphabet(),
    ):
        """
        :param alphabet: The alphabet to use.
        """
        self.output_mode = output_mode
        self.alphabet = alphabet

    def get_random_letter(self):
        """
        This function returns a random letter from the alphabet.
        """
        if self.output_mode == OutputMode.NORMAL:
            return self.alphabet.get_both_cases()[
                randint(0, len(self.alphabet.get_both_cases()) - 1)
            ]
        elif self.output_mode == OutputMode.VALID_INTERNET_USAGE:
            return self.alphabet.get_random_letter(letter_style="random")
        elif self.output_mode == OutputMode.VALID_FILE_NAME:
            return self.alphabet.get_random_letter(letter_style="lowercase")

    def get_random_letters(self, length: int):
        """
        This function returns a string of random letters from the alphabet.
        """
        return "".join([self.get_random_letter() for _ in range(length)])

    def get_random_number(self):
        """
        This function returns a random number.
        """
        return randint(0, 9)

    def get_random_numbers(self, length: int):
        """
        This function returns a string of random numbers.
        """
        return "".join([str(self.get_random_number()) for _ in range(length)])

    def get_random_string(self, length: int):
        """
        This function returns a random string.
        """
        combined_letters = (
            self.alphabet.get_both_cases()
            + self.alphabet.get_punctuation()
            + "0123456789"
        )
        return "".join(
            [
                combined_letters[randint(0, len(combined_letters) - 1)]
                for _ in range(length)
            ]
        )
