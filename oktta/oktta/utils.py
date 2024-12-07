import os
import string
import random

from dotenv import load_dotenv


load_dotenv()


def get_debug():
    return True if os.getenv('DEBUG') == 'True' else False


def get_email_ssl():
    return True if os.getenv('EMAIL_USE_SSL') == 'True' else False


def generate_password():
    letters = random.choices(string.ascii_letters, k=10)
    punctuation = random.choices(string.punctuation, k=2)
    digits = random.choices(string.digits, k=5)

    random.shuffle(password := letters + punctuation + digits)

    password = ''.join(password)

    return password
