#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for task 02"""


import datetime


class InvalidAgeError(Exception):
    """Class for an exception for age 0 or greater.

        Args:
            None

        Attributes:
            None
    """
    pass


def get_age(birthyear):
    """A small docstring for a function converting birth yr to age.

        Args:
            birthyear (int): An integer for the birth year.

        Returns:
            mixed: Integer for age and/or an error msg for wrong age.

        Examples:

            >>> get_age(2099)
            Trackback (most recent call last):
              File "<stdin>", line 1, in <module>
            __main__.InvalidAgeError
    """
    age = datetime.datetime.now().year - birthyear
    if age >= 0:
        return age
    else:
        raise InvalidAgeError
