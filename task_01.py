#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """Defines a function that looks up index or key values in a list.

        Args:
            var1 (mixed): a list, dictionary, or string value.
            var2 (mixed): an index or key value.

        Returns:
            mixed: Returns key and value, or error if invalid.

        Examples:
        >>> simple_lookup([1,2], 4)
        Warning: Your index/key doesn't exist
        [1,2]
    """
    try:
        return var1[var2]
    except LookupError:
        print 'Warning: Your index/key doesn\'t exist'
        return var1
