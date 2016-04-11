#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """ Sample function for testing exceptino handling.

    Args:
        var1 (string, list: or dictinary): object to be indexed or searched.
        var2 (int or key): index value or key to use for var1.

    Returns:
        (mixed): either result from index operation, value of key, or if
                an exception is raised, var1
    Examples:
        >>> s = 'this is a sample string'
        >>> d = {'a': 'simple', 'd': 'dictionary'}
        >>> simple_lookup(d, 'a')
        simple

        >>> simple_lookup(s, 20)
        Warning: index/key 20 doesn't exist
        'this is a sample string'
    """
    try:
        return var1[var2]
    except LookupError:
        print 'Warning: index/key {0} doesn\'t exist'.format(var2)
        return var1
