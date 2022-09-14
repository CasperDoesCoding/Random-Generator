from src.generators.chars import Chars


def test_chars():
    chars = Chars()
    # Test all the functions
    print("random letter:", chars.get_random_letter())
    print("random letters:", chars.get_random_letters(25))
    print("random number:", chars.get_random_number())
    print("random numbers:", chars.get_random_numbers(25))
    print("random string:", chars.get_random_string(25))


if __name__ == "__main__":
    test_chars()
