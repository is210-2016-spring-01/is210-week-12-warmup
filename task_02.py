#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """pass does nothing"""
    pass


def get_age(birthyear):
    """ checks if age is valid or not. If invalid: raise exception"""
    age = datetime.datetime.now().year - birthyear
    if age < 0:
        raise InvalidAgeError
    else:
        return age
