#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """Attempt a lookup of the first variable.

    Args:
        var1 (mixed): Dictionary to search for index.
        var2 (mised): Index attempt location.

    Returns:
        mixed: Key/value or error handling.

    Examples:
        >>> simple_lookup([1,2], 4)
        Warning: Your index/key doesn't exist.
        [1, 2]

        >>> simple_lookup({}, 'test')
        Warning: Your index/key doesn't exist.
        {}
    """
    try:
        return var1[var2]
    except LookupError:
        print 'Warning: Your index/key doesn\'t exist.'
        return var1
