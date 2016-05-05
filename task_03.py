#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """Custom class."""

    def __init__(self, logfilename):
        """__init__ docstring"""
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """Log function"""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """Flush function"""
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
