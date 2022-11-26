from MockDataGenerator.generators.NumericGenerators.NumericGenerator import RandomNumericGenerator


class RandomCpfGenerator:

    def __init__(self, valid=True):
        self._number_generator = RandomNumericGenerator(10)
        self._valid = valid

    def random_cpf(self):
        nums_cpf = [self._number_generator.random_integer(0, 10) for _ in range(9)]
        if self._valid:
            nums_cpf = self._calculate_digitos(nums_cpf)
        else:
            nums_cpf += [self._number_generator.random_integer(0, 10) for _ in range(2)]

        return "%d%d%d.%d%d%d.%d%d%d-%d%d" % tuple(nums_cpf)

    @staticmethod
    def _calculate_digitos(nums_cpf: list) -> list:
        while len(nums_cpf) < 11:
            s = sum(x * y for x, y in zip(nums_cpf, range(len(nums_cpf) + 1, 1, -1)))
            digito = 11 - s % 11
            if digito >= 10:
                digito = 0
            nums_cpf.append(digito)
        return nums_cpf


if __name__ == '__main__':
    gen = RandomCpfGenerator(valid=True)
    for i in range(5):
        print(gen.random_cpf())
