# -*- coding: utf-8 -*-
"""
Created on 9/30/20

@author dor
"""

import datetime
import random
import string
from typing import Union

from pymongo_odm.helpers.type_hints import Datetime


def random_int(start: int = 0, end: int = 100) -> int:
    """Return a random int between ``start`` and ``end``.

    Args:
        start (int): Minimum value to return.
        end (int): Maximum value to return.

    Returns:
        int: A random int between the start and end.
    """
    return random.randint(start, end)


def random_str(length: int = 10, unique: str = '') -> str:
    """Generate a random string

    Args:
        length (int): Optional. The length of the generated str.
        unique (str): Optional. Add a unique str to the end of the generated str
            (if you want to make sure that it's unique).

    Returns:
        str: randomly generated string
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length)) + unique


def random_dict(length: int = None) -> dict:
    """Generate a random dictionary with random values

    Args:
        length (int): Optional. Amount of items (key values) in the dict.

    Returns:
        dict: A randomly generated dictionary
    """
    d = {}
    for i in range(length or random.randint(1, 10)):
        d[str(i + random.random())] = random.uniform(10, 5000) * random.random() + random.randint(1, 500)

    return d


def random_datetime(min_year: int = 1900, max_year: int = 2025) -> Datetime:
    """Generate a random date between the min max dates.

    Args:
        min_year (int): Optional. Don't generate a date before this year.
        max_year (int): Optional. Don't generate a date after this year.

    Returns:
        Date: A randomly selected date.
    """
    return datetime.datetime(random.randint(min_year, max_year), random.randint(1, 12), random.randint(1, 28))
