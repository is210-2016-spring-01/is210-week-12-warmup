#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""I'm a lumberjack and I'm ok"""


import time


class CustomLogger(object):
    """CustomLogger Class."""

    def __init__(self, logfilename):
        """Constructor
        Attributes:
            None
        Args:
            longfilename(str)
            msgs(list)
        """
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """Method of logging
        Args:
            msg: Message from Log
            timestamp: Unix timestamp
        Returns:
            Log of messages.
        """
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """Flush Function"""
        handled = []

        try:
            fhandler = open(self.logfilename, 'a')
        except IOError:
            self.log('Logfile can not be opened.')
            raise IOError
        else:
            for index, entry in enumerate(self.msgs):
                try:
                    fhandler.write(str(entry) + '\n')
                    handled.append(index)
                except IOError:
                    self.log('I/O error.Can not write to file.')

        for index in handled[::-1]:
            del self.msgs[index]
        fhandler.close()
