#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """ Class for detecting invalid age
    """
    pass


def get_age(birthyear):
    """ A def docstring.

    Args:
        birthyear (int): Birthyear of person

    Returns:
        int:  Age of person

    Examples:
        >>> get_age(1933)
        83
        >>> get_age(2017)

        Traceback (most recent call last):
        File "<pyshell#1>", line 1, in <module>
        get_age(2017)
        File "/home/vagrant/Desktop/is210-week-12-warmup/task_02.py",
        line 34, in get_age
        raise InvalidAgeError
        InvalidAgeError
    """

    age = datetime.datetime.now().year - birthyear
    if age < 0:
        raise InvalidAgeError
    else:
        return age
