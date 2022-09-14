from generators.chars import Chars
from alphabets.swedish import SwedishAlphabet
from generators.chars import OutputMode


def main():
    chars = Chars(OutputMode.VALID_INTERNET_USAGE, SwedishAlphabet())
    print(chars.get_random_letters(25))


if __name__ == "__main__":
    main()
