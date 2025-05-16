import cmd
import json
import uuid
from datetime import datetime

class BaseModel:
    """A simple BaseModel class."""
    
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f"[BaseModel] ({self.id}) {self.__dict__}"

class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""
    
    prompt = '(hbnb) '
    storage = {}

    def do_create(self, class_name):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not class_name:
            print("** class name missing **")
            return
        if class_name != 'BaseModel':
            print("** class doesn't exist **")
            return
        
        new_instance = BaseModel()
        self.storage[new_instance.id] = new_instance
        self.save_to_file()
        print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id."""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != 'BaseModel':
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        instance_id = args[1]
        instance = self.storage.get(instance_id)
        if instance is None:
            print("** no instance found **")
        else:
            print(instance)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != 'BaseModel':
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        instance_id = args[1]
        if instance_id in self.storage:
            del self.storage[instance_id]
            self.save_to_file()
        else:
            print("** no instance found **")

    def do_all(self, class_name):
        """Prints all string representation of all instances based or not on the class name."""
        if class_name and class_name != 'BaseModel':
            print("** class doesn't exist **")
            return
        
        instances = [str(instance) for instance in self.storage.values()]
        print(instances)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != 'BaseModel':
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        instance_id = args[1]
        instance = self.storage.get(instance_id)
        if instance is None:
            print("** no instance found **")
            return
        
        if len(args) < 3:
            print("** attribute name missing **")
            return
        
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        
        attribute_value = args[3].strip('"')
        setattr(instance, attribute_name, attribute_value)
        instance.updated_at = datetime.now()
        self.save_to_file()

    def save_to_file(self):
        """Saves instances to a JSON file."""
        with open('file.json', 'w') as f:
            json.dump({k: v.__dict__ for k, v in self.storage.items()}, f)

    def emptyline(self):
        """Override emptyline method to do nothing on empty input."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF."""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
