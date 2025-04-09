import random
import string
from pathlib import Path
import os

class Data:
    @staticmethod
    def generate_random_string(length:int):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    COOKIE_RECIPE = {
        'name': 'Торт',
        'ingredient': 'шоколад белый',
        'weight': '500',
        'time': '3',
        'description': 'Только шоколад',
        'photo': os.path.join(os.path.dirname(__file__), 'test_data', 'торт.jpg')
    }