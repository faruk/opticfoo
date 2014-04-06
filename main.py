'''
Author: Jan Swoboda
Date: April - July 2013

Copyright 2013

LEGAL INFO:

This file is part of opticfoo (virtual room VJ concept - VRC in short).

Opticfoo is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Opticfoo is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
'''

from vrc import VRC
import sys

if __name__ == "__main__":
    x = 1600 
    y = 900
    try:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    except IndexError:
        print "running with standard 800x600 window for output"
        print 'use "python main.py <xValue> <yValue>" to adjust output window size'
    App = VRC(x, y)
    print "done"
    App.run()
