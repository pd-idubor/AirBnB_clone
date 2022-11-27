#!/usr/bin/python3
"""
    Describes the HBNB class
"""
import cmd
from models import storage
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
        Defines the the entry point of the command interpreter
    """
    prompt = "(hbnb) "
    classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
        }

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
            storage.save()
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

        r_obj = storage.all()
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

        r_obj = storage.all()
        key = arg_l[0] + "." + arg_l[1]

        try:
            del r_obj[key]

        except KeyError:
            print("** no instance found **")
        storage.save()

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
        objs = storage.all()
        obj_list = []
        
        for objs in storage.all().values():
            if (len(arg) > 0):
                if (arg[0] == objs.__class__.__name__):
                    obj_list.append(objs.__str__())
            elif (len(arg) == 0):
                obj_list.append(objs.__str__())
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

        r_obj = storage.all()
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
            obj_val = r_obj[key]
        except KeyError:
            print("** value missing **")
        
        try:
            attr_t = type(getattr(obj_val, arg_l[2]))
            arg_l[3] = attr_t(arg_l[3])
        except AttributeError:
            pass
        setattr(obj_val, arg_l[2], arg_l[3])
        storage.save()

    def default(self, args):
        """
            Catches funcions of dot notation, default for invalid input
        """
        func_args = {
                "all": self.do_all,
                }
        args = (args.replace("(", ".").replace(")", ".")
                .replace('"', "").replace(",", "").split("."))

        try:
            print(args)
            cmd_arg = args[0] + " " + args[2]
            func = func_args[args[1]]
            func(cmd_arg)
        except:
            print("*** Unknown syntax:", args[0])

    def emptyline(self):
        """Executes nothing upon receiving an empty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
