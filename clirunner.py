#!/usr/bin/env python
#
# A command line runner..
#
# Copyright (C) 2011 Senko Rasic <senko.rasic@dobarkod.hr>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import inspect
import sys


class CLIRunner(object):
    """
    Command line runner wrapper. Exposes methods as commands, makes sure
    they're called with the correct number of (string) arguments, and
    automatically generates the method description and help.
    """

    def __init__(self):
        self._app_name = self.__class__.__name__
        self._app_desc = self.__doc__.strip() if self.__doc__ else ''
        self._file_name = sys.argv[0]
        self._discover_commands()
        if self._dispatch():
            sys.exit(0)
        else:
            sys.exit(1)

    def _discover_commands(self):
        self._commands = []
        for name, meth in inspect.getmembers(self, inspect.ismethod):
            if name.startswith('_'):
                continue

            desc = meth.__doc__.strip() if meth.__doc__ else ''
            args = [arg.upper() for arg in inspect.getargspec(meth).args][1:]
            name = name.replace('_', '-')
            self._commands.append((name, args, desc, meth))

    def _dispatch(self):
        if len(sys.argv) == 1:
            self.help()
            return False

        cmd = sys.argv[1]
        args = sys.argv[2:]

        for name, specs, desc, meth in self._commands:
            if cmd == name:
                if len(args) != len(specs):
                    print "Command '%s' needs %d arguments, %d given." % (
                        cmd, len(specs), len(args))
                    if len(specs) > 0:
                        print "Usage: %s %s %s" % (self._file_name,
                        cmd, ' '.join(specs))
                    return False
                else:
                    return meth(*args)

        print "Command '%s' not recognized, try 'help' instead." % cmd
        return False

    def help(self):
        """
        Show this help.
        """
        print "%s - %s" % (self._app_name, self._app_desc)
        print "Usage: %s COMMAND [ARGS...]" % (self._file_name)
        print "Commands:"
        for name, args, desc, meth in self._commands:
            if len(args) > 0:
                argspec = ' ' + ' '.join(args)
            else:
                argspec = ''
            print "  %s%s - %s" % (name, argspec, desc)


if __name__ == '__main__':
    CLIRunner()
