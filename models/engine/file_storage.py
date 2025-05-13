#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects"""
        if cls is None:
            return self.__objects
        else:
            filtered_obj = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    filtered_obj[key] = value
            return filtered_obj

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.__class__.__name__ + '.' + obj.id: obj})

    def delete(self, obj=None):
        """Deletes obj from objects"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, 'w') as f:
            temp = {}
            temp.update(self.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        
        classes = {
            'BaseModel': BaseModel
        }
        
        try:
            if os.path.isfile(self.__file_path):
                with open(self.__file_path, 'r') as f:
                    temp = json.load(f)
                    for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except Exception:
            pass

    def close(self):
        """Deserialize the JSON file to objects"""
        self.reload()
