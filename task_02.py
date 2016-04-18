#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """Excetion that stores InvalidAgeError data."""
    pass


def get_age(birthyear):
    """Function that calculates age.

    Args:
        birthyear (int): the year

    Return:
        age (int): the age

    Examples:

        >>> get_age(2099)
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        __main__.InvalidAgeError
    """
    age = datetime.datetime.now().year - birthyear
    if age >= 0:
        return age
    else:
        raise InvalidAgeError
