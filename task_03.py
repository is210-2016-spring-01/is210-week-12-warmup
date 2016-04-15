#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for task 03"""


import time


class CustomLogger(object):
    """Class that uses an object for a logger"""

    def __init__(self, logfilename):
        """A dosctring for a constructor that uses the CustomLogger class"""
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """A docstring for a log function"""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """A doctring for a flush"""
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
