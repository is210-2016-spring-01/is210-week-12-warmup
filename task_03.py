#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """Creates a class for the logger"""

    def __init__(self, logfilename):
        """Creates a constructor for the CustomLogger class"""
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """Defines a logging function."""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """Defines the flush function."""
        handled = []

        try:
            fhandler = open(self.logfilename, 'a')
        except IOError:
            self.log('IOError encountered.')
            raise IOError
        try:
            for index, entry in enumerate(self.msgs):
                fhandler.write(str(entry) + '\n')
                handled.append(index)
        except IOError:
            self.log('IOError encountered.')
        finally:
            fhandler.close()

        for index in handled[::-1]:
            del self.msgs[index]
