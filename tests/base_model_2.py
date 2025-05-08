#!/usr/bin/python3
from models.base_model import BaseModel

bm = BaseModel()
print(type(bm.id) is str)
print(len(bm.id) > 0)

