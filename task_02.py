#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """Ths class identifies invalid ages."""
    pass


def get_age(birthyear):
    """This function calculates age."""
    age = datetime.datetime.now().year - birthyear
    if age < 0:
        raise InvalidAgeError()
    else:
        return age
