#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """Looks up keys, lists.
    Attributes:
        var1 (list): a list
        var2 (int): index of var1
    Returns:
        var1[var2]: element and key. will error if it doesn't exist.
     Example:
        >>> simple_lookup([1,5], 1)
        5
        """
    try:
        return var1[var2]
    except LookupError:
        print 'Warning: Your index/key doesn\'t exist.'
        return var1
