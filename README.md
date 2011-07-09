# Command Line Runner

A Python module for easily getting the arguments from the command
line, and selecting which command to run. Way simpler than optparse
or argparse modules, use it when you don't the full power of those
libraries.

### Usage

Subclass the CLIRunner class. Add methods to expose as commands. If you
don't want to expose a particular method, prefix it by underscore. If the
method name contains an underscore somewhere in the middle, the
corresponding command will have a hypen instead.

Docstrings are used for help. Set the class docstring for the
app/binary overview, and the method docstrings for the command help.
Use only positional arguments (*args) in methods. The argument names
will be shown (in uppercase) in the help output.

The help output is provided by the CLIRunner.hello() method. You can
override it if you want to customise it further.

To activate the wrapper, just create a new object of your subclass.

### Example

The code:

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

End result:

    $ python example.py
    HelloWorld - A simple Hello World application.
    Usage: example.py COMMAND [ARGS...]
    Commands:
      hello NAME - Greets you by name.
      hello-world - Print standard greeting.
      help - Show this help.

    $ python example.py hello
    Command 'hello' needs 1 arguments, 0 given.
    Usage: example.py hello NAME

    $ python example.py hello-world
    Hello World!

### License

Licensed under MIT license. Forks and pull-requests (and bug reports) are welcome.