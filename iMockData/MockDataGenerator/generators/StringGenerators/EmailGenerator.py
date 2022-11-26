import random
import json
from MockDataGenerator.generators.StringGenerators.NameGenerator import RandomNameGenerator


class RandomEmailGenerator:

    def __init__(self, providers_path):
        self._load_email_providers(providers_path)
        self._name_generator = RandomNameGenerator()

    def random_email(self):
        username = self._name_generator.get_first_name() + self._name_generator.get_last_name()
        mail_server = random.choice(self._providers)
        return username + '@' + mail_server

    def _load_email_providers(self, providers_path):
        with open(providers_path, 'r') as f:
            providers_json = json.load(f)
            self._providers = providers_json['email_providers']


if __name__ == '__main__':
    gen = RandomEmailGenerator('../lib/EmailProviders.json')
    print(gen.random_email())
