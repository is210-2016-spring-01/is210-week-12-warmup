#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """class docstring for an exception"""
    pass

def get_age(birthyear):
    """Tests if age provided is greater than 0.
    Attributes:
        birthyear (int): year that person was born
    Returns:
        age (int): person's age or error if less than 0
    Example:
        >>>get_age(2000)
        16
    age = datetime.datetime.now().year - birthyear
    if age < 0:
        raise InvalidAgeError()
    return age
