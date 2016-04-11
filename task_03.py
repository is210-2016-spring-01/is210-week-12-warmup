#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """A custom log class"""

    def __init__(self, logfilename):
        """A constructor for CustomLogger class"""
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """A logging function"""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """A flush function"""
        handled = []

        try:
            fhandler = open(self.logfilename, 'a')
        except IOError as err:
            self.log('Cannot be opened', time.time)
            raise err
        for index, entry in enumerate(self.msgs):
            try:
                fhandler.write(str(entry) + '\n')
                handled.append(index)
            except IOError:
                self.log('IO error', time.time)
                break
            except BaseException:
                self.log('Any other error', time.time)

        fhandler.close()

        for index in handled[::-1]:
            del self.msgs[index]
