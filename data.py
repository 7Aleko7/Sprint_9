import random
import string
from pathlib import Path

class Data:
    @staticmethod
    def generate_random_string(length:int):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    home =Path.home()
    cookie_photo = Path(home, 'PycharmProjects', 'Sprint_9','торт.jpg')

    COOKIE_RECIPE = {
        'name': 'Торт',
        'ingredient': 'шоколад белый',
        'weight': '500',
        'time': '3',
        'description': 'Только шоколад',
        'photo': str(cookie_photo)
    }