#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """This docstring illustrates the error handling principle.

    Args:
        var1(mixed): A dictionary
        var2 (empty): A empty dictionary that will not return item accessed.

    Returns:
        mixed: Key/value accessed or a warning statement.

    Examples:
        >>>simple_lookup([a:3, 5, 7], [b: 2]
        Warning: Your index/key does not exist.
        [3, 5, 7]

        >>>simple look_up([3, 5, 7], [a:1]
        Warning: Your index/key does not exist.
        [3, 5, 7]
        """
    try:
        var2[var1]
    except IndexError:
        print 'Warning: Your index/key doesn\'t exist.'
    return var1
