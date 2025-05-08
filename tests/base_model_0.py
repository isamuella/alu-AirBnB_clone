from models.base_model import BaseModel
from time import sleep

bm = BaseModel()
first_time = bm.updated_at
sleep(1)
bm.save()
print(bm.updated_at > first_time)
