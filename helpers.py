from faker import Faker
import string
import random


class Helpers:
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def generate_random_email(self):
        fake = Faker()
        return fake.email()

    def generate_random_name(self):
        fake = Faker()
        return fake.name()
