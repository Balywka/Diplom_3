import random
import string

class TestData:
    @staticmethod
    def generate_random_string(length=8):
        return "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

    @staticmethod
    def generate_user_data():
        rnd = TestData.generate_random_string()
        return {
            "email": f"Osipova_{rnd}@yandex.ru",
            "password": "Password123!",
            "name": f"Osipova_{rnd}",
        }