#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """Exception if age is not greater or equal to 0."""
    pass


def get_age(birthyear):
    """Check that age is greater or equal to 0."""
    age = datetime.datetime.now().year - birthyear
    if age >= 0:
        return age
    else:
        raise InvalidAgeError
