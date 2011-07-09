#!/usr/bin/env python

from clirunner import CLIRunner


class HelloWorld(CLIRunner):
    "A simple Hello World application."

    def hello_world(self):
        "Print standard greeting."
        print "Hello World!"

    def hello(self, name):
        "Greets you by name."
        print "Hello, %s!" % name

if __name__ == '__main__':
    HelloWorld()
