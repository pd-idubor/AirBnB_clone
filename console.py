#!/usr/bin/python3
"""
    Describes the HBNB class
"""
import cmd
import models
import shlex
from models.base_model import BaseModel


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

    def do_create(self, args):
        """Creates a new instance of BaseModel and prints the id
        """
        arg_l = shlex.split(args)

        if (len(arg_l) == 0):
            print("** class name missing **")
            return
        try:
            instance = eval(arg_l[0])()
            instance.save()
            print(instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance
        """
        arg_l = shlex.split(args)

        if (len(arg_l) == 0):
            print("** class name missing **")
            return

        try:
            eval(arg_l[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if (len(arg_l) == 1):
            print("** instance id missing **")
            return

        r_obj = models.storage.all()
        key = arg_l[0] + "." + arg_l[1]
        try:
            val = r_obj[key]
            print(val)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        """
        arg_l = shlex.split(args)

        if (len(arg_l) == 0):
            print("** class name missing **")
            return

        try:
            eval(arg_l[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if (len(arg_l) == 1):
            print("** instance id missing **")
            return

        r_obj = models.storage.all()
        key = arg_l[0] + "." + arg_l[1]

        try:
            del r_obj[key]

        except KeyError:
            print("** no instance found **")
        models.storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances
        """
        arg = shlex.split(args)

        if (len(args) > 0):
            try:
                eval(args)
            except NameError:
                print("** class doesn't exist **")
                return
        objs = models.storage.all()
        obj_list = []
        for key, val in objs.items():
            if (len(arg) > 0):
                if (arg[0] == val['__class__']):
                    obj_list.append(val)
            else:
                obj_list.append(val)
        print(obj_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id
        """
        arg_l = shlex.split(args)

        if (len(arg_l) == 0):
            print("** class name missing **")
            return

        try:
            eval(arg_l[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if (len(arg_l) == 1):
            print("** instance id missing **")
            return

        r_obj = models.storage.all()
        key = arg_l[0] + "." + arg_l[1]
        try:
            val = r_obj[key]
        except KeyError:
            print("** no instance found **")
            return

        if (len(arg_l) == 2):
            print("** attribute name missing **")
            return

        try:
            r_obj[key][arg_l[2]] = arg_l[3]

        except IndexError:
            print("** value missing **")
        models.storage.save()

    def emptyline(self):
        """Executes nothing upon receiving an empty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
