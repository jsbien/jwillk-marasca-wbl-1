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

import os

TEMPLATE_DEBUG = DEBUG = False

ADMINS = MANAGERS = ()

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
)

if DEBUG:
    MIDDLEWARE_CLASSES += (
        'utils.profiling.ProfilingMiddleware',
    )

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    'templates/',
)

INSTALLED_APPS = (
    'django.contrib.sessions',
)

SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
# PickleSerializer is a bad idea for the cookie backend,
# but it's okay for the file backend.
# https://docs.djangoproject.com/en/1.5/topics/http/sessions/#using-cookie-based-sessions
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

def _(x): return x

USE_I18N = True
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('pl', _('Polish')),
    ('en', _('English')),
)
LOCALE_PATHS = (
    os.path.join(
        os.path.dirname(__file__),
        os.pardir,
        'locale',
    ),
)

SESSION_LOCKS_DIRECTORY = '../locks/'
SESSION_LOCK_TIMEOUT = 5

BUFFER_SIZE = 1000
NOTIFICATION_INTERVAL = 10
MAX_RANDOM_SAMPLE_SIZE = BUFFER_SIZE
MAX_RESULTS_PER_PAGE = 1000
QUERY_TIMEOUT = 0.5

# By default poliqarpd restricts life-time of an idle session to 1200 seconds.
# See max-session-idle setting in poliqarpd(1).
# This value should be *lower* than that one.
SESSION_REFRESH = 1000

try:
    from .secret_key import SECRET_KEY
except ImportError, ex:
    import sys
    print >>sys.stderr, 'Please run the setup script to create an initial configuration.'
    sys.exit(1)

def _get_hostname():
     import socket
     hostname = socket.gethostname()
     hostname = hostname.split('.')[0]
     return hostname
_hostname = _get_hostname()
_module = getattr(__import__('', locals(), globals(), [_hostname], 1), _hostname)
_data = dict((k, v) for k, v in vars(_module).items() if not k.startswith('_'))
vars().update(_data)
del _data, _module, _hostname, _get_hostname

# vim:ts=4 sw=4 et
