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

_locale_map = dict(
	en = 'en_US',
	pl = 'pl_PL',
)

_default_locale = 'en_US'

def get_locale(language_code):
	# FIXME: Move handling of .UTF-8 suffix into poliqarpd
	return _locale_map.get(language_code, _default_locale) + '.UTF-8'

# vim:ts=4 sw=4 noet
