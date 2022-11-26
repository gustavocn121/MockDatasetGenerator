import string
from MockDataGenerator.generators.NumericGenerators.NumericGenerator import RandomNumericGenerator
from random import choice


class RandomStringGenerator:
    _uppercase_letters = [*string.ascii_uppercase]
    _lowercase_letters = [*string.ascii_lowercase]
    _digits = [*string.digits]
    _punctuation = [*string.punctuation]
    _characters = [None]

    def __init__(self, min_length=0, max_length=10, upper_case=True, lower_case=True,
                 digits=False, punctuation=False, blank=False):
        if min_length < 0:
            min_length = 0
        if max_length < min_length:
            max_length = min_length

        self.characters = self._generate_character_set(upper_case, lower_case, digits, punctuation, blank)
        self._min_length = min_length
        self._max_length = max_length
        self._number_generator = RandomNumericGenerator()

    def _generate_character_set(self, upper_case, lower_case, digits, punctuation, blank) -> list:
        characters = []
        if upper_case:
            characters += self._uppercase_letters
        if lower_case:
            characters += self._lowercase_letters
        if digits:
            characters += self._digits
        if punctuation:
            characters += self._punctuation

        if blank or not characters:
            characters += ' '

        return characters

    @property
    def characters(self):
        return self._characters

    @characters.setter
    def characters(self, char_list: list):
        self._characters = char_list

    def random_char(self):
        return choice(self._characters)

    def random_simple_string(self):
        length = self._number_generator.random_integer(self._min_length, self._max_length)
        return ''.join([self.random_char() for _ in range(length)]).strip()


if __name__ == '__main__':
    gen = RandomStringGenerator(min_length=1, max_length=10, upper_case=True, lower_case=True,
                                digits=False, punctuation=False, blank=True)
    s = gen.random_simple_string()
    print(s)
    print(len(s))
