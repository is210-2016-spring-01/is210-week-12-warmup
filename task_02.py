#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """Creates a class for the exception.

        Args:
            None

        Attributes:
            None
    """
    pass


def get_age(birthyear):
    """Defines a function to determine age based on birth year/current date.

        Args:
            birthyear (int): An integer representing the year of birth.

        Returns:
            mixed: integer for age, or error message if invalid age.

        Example:
            >>>get_age(1989)
            27
    """
    age = datetime.datetime.now().year - birthyear
    if age >= 0:
        return age
    else:
        raise InvalidAgeError
