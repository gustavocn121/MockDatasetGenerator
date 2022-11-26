import names


class RandomNameGenerator:

    @staticmethod
    def get_full_name():
        return names.get_full_name()

    @staticmethod
    def get_first_name():
        return names.get_first_name()

    @staticmethod
    def get_last_name():
        return names.get_first_name()


if __name__ == '__main__':
    gen = RandomNameGenerator()
    print(gen.get_full_name())
    print(gen.get_first_name())
    print(gen.get_last_name())
