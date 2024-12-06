import os

from dotenv import load_dotenv


load_dotenv()


def get_debug():
    return True if os.getenv('DEBUG') == 'True' else False


def get_email_ssl():
    return True if os.getenv('EMAIL_USE_SSL') == 'True' else False
