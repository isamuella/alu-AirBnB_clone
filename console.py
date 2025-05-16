#!/usr/bin/python3
"""
A program called console.py that contains the entry point of the command interpreter:

"""
import cmd
from models import storage

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

    def help_quit(self):
        """help for the quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """helf for the EOF command"""
        print("Exit the program with EOF")

    def do_create(self, class_name):
        """Creates a new instance, saves to json, and prints the id"""
        if not class_name:
            print("** class name missing **")
            return
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return

        new_instance = storage.new(class_name)
        storage.save()
        print(new_instance.id)

    def do_show(self, args):
        """prints the string representation of an instance based on the classname and id"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != "BaseModel":
            print("**class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        instance = storage.get(class_name, instance_id)
        if instance is None:
            print("** no instance found **")
        else:
            print(instance)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        if storage.delete(class_name, instance_id):
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name"""
        if class_name and class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        instances = storage.all(class_name)
        print([str(instance) for instance in instances])

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = args.split()
        if not args:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
