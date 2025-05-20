#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel

classes = {
    "BaseModel": BaseModel
}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, args):
        if not args:
            print("** class name missing **")
            return
        if args not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[args]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        tokens = args.split()
        if len(tokens) == 0:
            print("** class name missing **")
        elif tokens[0] not in classes:
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        else:
            key = f"{tokens[0]}.{tokens[1]}"
            obj = storage.all().get(key)
            if obj:
                print(obj)
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        tokens = args.split()
        if len(tokens) == 0:
            print("** class name missing **")
        elif tokens[0] not in classes:
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        else:
            key = f"{tokens[0]}.{tokens[1]}"
            obj_dict = storage.all()
            if key in obj_dict:
                del obj_dict[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        result = []
        if args:
            if args not in classes:
                print("** class doesn't exist **")
                return
            for obj in storage.all().values():
                if obj.__class__.__name__ == args:
                    result.append(str(obj))
        else:
            for obj in storage.all().values():
                result.append(str(obj))
        print(result)

    def do_update(self, args):
        tokens = args.split()
        if len(tokens) == 0:
            print("** class name missing **")
        elif tokens[0] not in classes:
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        else:
            key = f"{tokens[0]}.{tokens[1]}"
            obj = storage.all().get(key)
            if not obj:
                print("** no instance found **")
            elif len(tokens) == 2:
                print("** attribute name missing **")
            elif len(tokens) == 3:
                print("** value missing **")
            else:
                attr_name = tokens[2]
                attr_value = tokens[3].strip("\"'")
                # Try to cast value
                try:
                    casted_value = eval(attr_value)
                except Exception:
                    casted_value = attr_value
                setattr(obj, attr_name, casted_value)
                obj.save()

    def do_EOF(self, arg):
        """Handles EOF to exit program"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

