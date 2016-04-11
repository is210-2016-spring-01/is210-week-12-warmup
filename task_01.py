#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""simple_lookup"""


def simple_lookup(var1, var2):
    """Function that looks up keys and lists
    Attributes:
        var1 (list): A list of items
        var2 (int): Index of list.
    Returns:
        var1[var2]: The element and key are returned as var1[var2]
    Example:
        >>> simple_lookup([1,3], 1)
        3
    """

    try:
        return var1[var2]
    except LookupError:
        print 'Warning: Your index/key doesn\'t exist.'
        return var1
