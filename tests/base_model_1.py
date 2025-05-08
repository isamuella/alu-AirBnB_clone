#!/usr/bin/python3
from models.base_model import BaseModel

bm = BaseModel()
bm.name = "My Model"
bm.number = 42
bm_dict = bm.to_dict()
print("__class__" in bm_dict)
print("created_at" in bm_dict)
print("updated_at" in bm_dict)
print(type(bm_dict["created_at"]) is str)
print(type(bm_dict["updated_at"]) is str)

