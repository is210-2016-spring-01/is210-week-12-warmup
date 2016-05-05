#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """CustomLogger class"""

    def __init__(self, logfilename):
        """constructor
        Attributes:
            None
        Args:
            longfilename (str)
            msgs(list)
        """
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """How the logging comes to be
        Args:
            msg: log message
            timestamp: system's timestamp
         Returns:
            log of msgs
         """
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """modified this...so that predictable errors get caught"""
        handled = []

        try:
            fhandler = open(self.logfilename, 'a')
        except IOError:
            self.log('Cannot open logfile!')
            raise IOError
        else:
            for index, entry in enumerate(self.msgs):
                try:
                    fhandler.write(str(entry) + '\n')
                    handled.append(index)
                except IOError:
                    self.log('I/O error. Cannot write to file!')

        for index in handled[::-1]:
            del self.msgs[index]
        fhandler.close()
