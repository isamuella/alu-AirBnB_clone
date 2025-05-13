#!/usr/bin/python3
"""
A program called console.py that contains the entry point of the command interpreter:

"""
import cmd

class HBNBCommand(cmd.Cmd):
    """Class that implements a command-line interface for the AirBnB clone application"""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """command to exit the program"""
        return True

    def do_EOF(self, arg):
        """command to exit the program after a new line"""
        print()
        return True

    def emptyline(self):
        """an empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
