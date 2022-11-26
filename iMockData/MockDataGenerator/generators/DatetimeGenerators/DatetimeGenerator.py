from datetime import datetime, timedelta
from random import randrange


class RandomDateGenerator:

    def __init__(self, initial_date=datetime.now() - timedelta(days=(365*10)), max_date=datetime.now() + timedelta(days=(365*5))):
        self.initial_date = initial_date
        self.max_date = max_date

    def random_datetime(self, date_format="%Y-%m-%d %H:%M:%S"):
        max_diff = self._max_date - self.initial_date
        seconds = randrange(0, int(max_diff.total_seconds()))
        date = self.initial_date + timedelta(seconds=seconds)
        return date.strftime(date_format)

    @property
    def initial_date(self):
        return self._initial_date

    @initial_date.setter
    def initial_date(self, new_initial_date: datetime):
        self._initial_date = new_initial_date

    @property
    def max_date(self):
        return self._max_date

    @max_date.setter
    def max_date(self, new_max_date: datetime):
        self._max_date = new_max_date


if __name__ == '__main__':
    date_gen = RandomDateGenerator(datetime.now() - timedelta(days=(365*3)), datetime.now())
    random_date = date_gen.random_datetime("%Y/%m/%d %H:%M:%S")
    print(random_date)
