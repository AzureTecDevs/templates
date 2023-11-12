import cmd

class cmd(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '> '

    def do_hello(self, arg):
        print "Hello, ", arg, "!"

    def do_quit(self, arg):
        sys.exit(1)

cli = cmd()
cli.cmdloop()
