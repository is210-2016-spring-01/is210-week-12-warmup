#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """ A def docstring.

    Args:
        var1 (mixed): A variable
        var2 (mixed): A variable

    Returns:
        Mixed:  A varible and/or string

    Examples:
        >>> simple_lookup([1,2], 4)
        Warning Key or Index Error
        [1, 2]
    """
    try:
        return var1[var2]
    except LookupError:
        print 'Key or Index Error does not exists'
        return var1
