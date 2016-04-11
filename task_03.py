#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """ Custom Logger class for testing the finally process.

    Args:
        none.

    Attributes:
        none.
    """

    def __init__(self, logfilename):
        """ constructor for CustomerLogger testing class

        Args:
            logfilename (string): name of file to receive logging messages

        Attributes:
            logfilename (string): name of file to receive logging messages
            msgs (list): list of messages for the log file.
        """

        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """ function to add a message to be written to the log file.

        Args:
            msg (string): message to queue for the log file.
            timestampe (time): time value to assign to log mesasge, or None for
                                current time.

        Returns:
            nothing.

        Examples:
            >>> cl = CustomLogger()
            >>> cl.log('this is a message for the log')
        """
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """ writes out all messages queued for the log file and closes the file.

        Args:
            none.

        Returns:
            nothing.

        Examples:
            >>> cl = CustomLogger()
            >>> cl.flush()
        """
        handled = []

        try:
            fhandler = open(self.logfilename, 'a')
        except IOError as ioe:
            self.log('I/O error {0} openning {1}, {2}'.format(ioe.errno,
                                                              self.logfilename,
                                                              ioe.strerror))
            raise ioe

        try:
            for index, entry in enumerate(self.msgs):
                fhandler.write(str(entry) + '\n')
                handled.append(index)
        except IOError as ioe:
            self.log('I/O error {0} writting to log, {1}'.format(ioe.errno,
                                                                 ioe.strerror))

        finally:
            fhandler.close()

            for index in handled[::-1]:
                del self.msgs[index]
