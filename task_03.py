#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """This class creates logs."""

    def __init__(self, logfilename):
        """Creates Logfilemane.
        Attributes:
            None
        Arguments:
            logfilename(string)
            msgs(list)
        """
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """Creates a timestamp.
        Attributes:
            None
        Arguments:
            msgs(list)
            timestamp(integer)
        """
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """A flush function."""
        handled = []
        try:
            fhandler = open(self.logfilename, 'a')
        except IOError:
            self.log('Logfile cannot be opened.')
            raise IOError
        else:
            for index, entry in enumerate(self.msgs):
                try:
                    fhandler.write(str(entry) + '\n')
                    handled.append(index)
                except IOError:
                    self.log('I/O error. File cannot be written to.')
        for index in handled[::-1]:
            del self.msgs[index]
        fhandler.close()
