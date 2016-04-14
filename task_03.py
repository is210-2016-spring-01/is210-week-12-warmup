#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """Python logging class."""

    def __init__(self, logfilename):
        """Instance of CustomLogger."""
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """Timestamp the log."""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """Add messages to log."""
        handled = []
        fhandler = open(self.logfilename, 'a')
        try:
            for index, entry in enumerate(self.msgs):
                fhandler.write(str(entry) + '\n')
                handled.append(index)
        except IOError:
            self.log('IOError logged.')

        try:
            for index in handled[::-1]:
                del self.msgs[index]
        except IOError:
            self.log('IOError logged.')
        except StandardError as sderror:
            self.log('{0} logged.'.format(sderror))
        finally:
            fhandler.close()
