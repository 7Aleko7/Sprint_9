import random
import string
import os

class Data:
    @staticmethod
    def generate_random_string(length:int):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    photo_path = os.path.join(os.path.dirname(__file__), "торт.jpg")

    COOKIE_RECIPE = {
        'name': 'Торт',
        'ingredient': 'шоколад белый',
        'weight': '500',
        'time': '3',
        'description': 'Только шоколад',
        'photo': str(photo_path)
    }