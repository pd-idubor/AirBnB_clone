#!/usr/bin/python3
"""
    Describes the HBNB class
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
        Defines the the entry point of the command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """EOF signal to exit the program
        """
        return True

    def emptyline(self):
        """Executes nothing upon receiving an empty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
