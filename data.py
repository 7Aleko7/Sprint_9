import random
import string
from pathlib import Path

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
        'photo': str(Path(__file__).parent.parent / 'торт.jpg')
    }