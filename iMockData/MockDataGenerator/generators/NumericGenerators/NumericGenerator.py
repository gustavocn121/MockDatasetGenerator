from random import randrange, uniform


class RandomNumericGenerator:

    def __init__(self, init_value=0, stop_value=1_0000_00):
        self.init_value = init_value
        if stop_value == init_value:
            stop_value = init_value+1
        self.stop_value = stop_value

    def random_integer(self, init_value=None, stop_value=None) -> int:
        if init_value is None:
            init_value = self._init_value
        if stop_value is None:
            stop_value = self._stop_value
        return randrange(init_value, stop_value)

    def random_float(self, init_value=None, stop_value=None, decimals=2) -> float:
        if init_value is None:
            init_value = self._init_value
        if stop_value is None:
            stop_value = self._stop_value
        return round(uniform(init_value, stop_value), decimals)

    @property
    def init_value(self):
        return self._init_value

    @init_value.setter
    def init_value(self, value):
        self._init_value = value

    @property
    def stop_value(self):
        return self._stop_value

    @stop_value.setter
    def stop_value(self, value):
        self._stop_value = value


if __name__ == '__main__':
    randomNumericGenerator = RandomNumericGenerator()
    print(randomNumericGenerator.random_float(2))
    print(randomNumericGenerator.random_integer())

