from generators.DatetimeGenerators import DatetimeGenerator
from generators.NumericGenerators import NumericGenerator
from generators.StringGenerators import SimpleStringGenerator
from generators.StringGenerators import NameGenerator
from generators.StringGenerators import CpfGenerator
from generators.StringGenerators import EmailGenerator
import os
import pandas as pd

class DataframeGenerator:

    def __init__(self):
        self._data_types = {
            'datetime': ['datetime'],
            'numeric': ['integer', 'float'],
            'string': ['simple', 'cpf', 'email', 'name']
        }

        self._generators = {
            'datetime': DatetimeGenerator.RandomDateGenerator().random_datetime,
            'integer': NumericGenerator.RandomNumericGenerator(init_value=0, stop_value=1_000).random_integer,
            'float': NumericGenerator.RandomNumericGenerator(init_value=0, stop_value=1_000).random_float,
            'str': SimpleStringGenerator.RandomStringGenerator(min_length=3, max_length=10).random_simple_string,
            'cpf': CpfGenerator.RandomCpfGenerator(valid=True).random_cpf,
            'email': EmailGenerator.RandomEmailGenerator(providers_path=os.getcwd() + '/generators/lib/EmailProviders.json').random_email,
            'name': NameGenerator.RandomNameGenerator().get_full_name
        }

    def generate_pandas_df(self, columns_dict: dict, rows: int):
        df_data = {}

        for col_name, col_dtype in columns_dict.items():
            col_data = [self._generators[col_dtype]() for _ in range(rows)]
            df_data[col_name] = col_data

        return pd.DataFrame(data=df_data)


if __name__ == '__main__':
    # date_gen = DatetimeGenerator.RandomDateGenerator()
    # num_gen = NumericGenerator.RandomNumericGenerator(init_value=0, stop_value=1_000)
    # str_gen = SimpleStringGenerator.RandomStringGenerator(min_length=3, max_length=10)
    # cpf_gen = CpfGenerator.RandomCpfGenerator(valid=True)
    # email_gen = EmailGenerator.RandomEmailGenerator(providers_path=os.getcwd() + '/generators/lib/EmailProviders.json')
    # name_gen = NameGenerator.RandomNameGenerator()
    #
    # print(date_gen.random_datetime())
    # print(num_gen.random_integer())
    # print(str_gen.random_simple_string())
    # print(cpf_gen.random_cpf())
    # print(email_gen.random_email())
    # print(name_gen.get_full_name())

    df_generator = DataframeGenerator()
    columns = {
        'login_date': 'datetime',
        'user_document': 'cpf',
        'user_email': 'email',
        'user_name': 'name',
        'user_coins': 'integer',
        'pf_rarity': 'float'
    }

    df = df_generator.generate_pandas_df(columns_dict=columns, rows=100)
    print(df.to_string())
