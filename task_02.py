#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """Exception Class"""
    pass


def get_age(birthyear):
    """A Function that tests if ages are legal(greater than zero)"""
    age = datetime.datetime.now().year - birthyear
    if not age > 0:
        raise InvalidAgeError()
    return age
