#!/usr/bin/python2
# Copyright (C) 2019 OpenIO SAS, as part of OpenIO SDS
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
See how an HTTP request is read by an ASN.1 server.
"""

import sys

for verb in sys.argv[1:]:
    verb = verb[:4]
    if len(verb) < 4:
        verb = verb.ljust(4, ' ')
    bytes_ = [ord(x) for x in verb]
    int_ = sum(x * 2 ** y for x, y in zip(bytes_, (24, 16, 8, 0)))
    hex_ = ''.join('%X' % x for x in bytes_)
    print "# int      hex      ascii"
    print '%10d %8s "%s"' % (int_, hex_, verb)
