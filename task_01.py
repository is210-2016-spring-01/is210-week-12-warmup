#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """This docstring illustrates the error handling principle.

    Args:
        var1(mixed): A dictionary or list
        var2(mixed): An index or key
    Returns:
        mixed: Key/value accessed or a var1.

    Examples:
        >>>simple_lookup({'a':3, 'b':5, 'c':7}, 'd')
        Warning: Your index/key does not exist.
        {'a':3, 'b':5, 'c':7}

        >>>simple look_up([3, 5, 7], 8)
        Warning: Your index/key does not exist.
        [3, 5, 7]
        """
    try:
        return var1[var2]
    except IndexError:
        print 'Warning: Your index/key doesn\'t exist.'
    except KeyError:
        print 'Warning: Your index/key doesn\'t exist.'
    return var1
