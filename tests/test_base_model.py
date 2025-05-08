#!/usr/bin/python3
from models.base_model import BaseModel

my_example = BaseModel()
my_example.name = "My First Model"
my_example.my_number = 89
print(my_example)
my_example.save()
print(my_example)
my_example_json = my_example.to_dict()
print(my_example_json)
print("JSON of my_example:")
for key in my_example_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_example_json[key]), my_example_json[key]))
