# encoding=UTF-8

# Copyright © 2009, 2010 Jakub Wilk <jwilk@jwilk.net>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import errno
import fcntl
import os
import random
import time

from django.conf import settings

class SessionLock(object):

    def __init__(self, session, wait=None):
        self._filename = os.path.join(settings.SESSION_LOCKS_DIRECTORY, '%s.lock' % session.session_key)
        if wait is None:
            self._wait = settings.SESSION_LOCK_TIMEOUT
        else:
            self._wait = wait

    def __enter__(self):
        while 1:
            try:
                self._fd = os.open(self._filename, os.O_CREAT | os.O_RDWR | os.O_EXCL, 0600)
            except OSError, ex:
                if ex.errno != errno.EEXIST or self._wait <= 0:
                    raise
                sleep = random.random()
                if sleep > self._wait:
                    sleep = self._wait
                self._wait -= sleep
                time.sleep(sleep)
            else:
                break

    def __exit__(self, ex_type, ex_value, ex_traceback):
        os.unlink(self._filename)
        os.close(self._fd)

# vim:ts=4 sw=4 et
