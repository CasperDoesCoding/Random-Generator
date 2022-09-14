"""
    This generator generates random email addresses.

    Author: github.com/CasperDoesCode
"""
from enum import Enum


class IdentifierType(Enum):
    """
    Enum for the different types of identifiers.
    """

    HUMAN_NAME = 0
    RANDOM_CHARS = 1
    RANDOM_NUMBERS = 2
    RANDOM_STRING = 3


class Email:
    """
    This class generates a random email address.
    """

    def __init__(self):
        pass  # TODO: Implement
