#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for task 01"""


def simple_lookup(var1, var2):
    """A small docstring for a function that accesses an index or key.

    Args:
        var1 (mixed): A list, integer, dictionary, or string value.
        var2 (mixed): A list, integer, dictionary, or string value.

    Returns:
        mixed: Returns an error msg if index/key is missing.

    Examples:

        >>> simple_lookup([1,2], 4)
        Warning: Your index/key doesn't exist.
        [1, 2]

        >>> simple_lookup({}, 'banana')
        Warning: Your index/key doesn't exist.
        {}

    """
    try:
        return var1[var2]
    except LookupError:
        print 'Warning: Your index/key doesn\'t exist'
        return var1
