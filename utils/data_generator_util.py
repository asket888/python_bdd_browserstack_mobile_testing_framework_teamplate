import random
import string
import time
from datetime import datetime


def get_random_string(length: int) -> str:
    """
    Generate random string with chosen length
    :return: random string
    """
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def get_unique_integer() -> int:
    """
    Generate unique integer according to current timestamp
    :return: unique int
    """
    return int(time.time())


def get_current_date_and_time():
    """
    Generate current date in ("%d/%m/%Y %H:%M:%S") format
    :return: current date and time
    """
    now = datetime.now()
    formatted_date = now.strftime("%Y/%m/%d %H:%M:%S")
    return formatted_date
