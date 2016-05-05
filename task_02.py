#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """ Exception class.

    Args:
        none.

    Attributes:
        none.
    """
    pass


def get_age(birthyear):
    """ Sample function to calaculate age i years and raise exception if not
        valid.

    Args:
        birthyear (int): year of birth.

    Returns:
        int: age in full years.

    Examples:
        >>> get_age(1999)
        16

        >>> get_age(2099)
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        __main__.InvalidAgeError
    """
    age = datetime.datetime.now().year - birthyear
    if age >= 0:
        return age

    raise InvalidAgeError()
