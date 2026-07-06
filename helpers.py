import random
import string

class CourierGenerator:
    @staticmethod
    def generate_random_string(length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def get_random_courier_data():
        return {
            "login": CourierGenerator.generate_random_string(),
            "password": CourierGenerator.generate_random_string(),
            "firstName": CourierGenerator.generate_random_string()
        }