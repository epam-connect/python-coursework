from pydantic import BaseModel, StrictInt

class A(BaseModel, strict=True):
    x : int # StrictInt to enforce
    y : int


obj = A(x=10, y=20)
obj1 = A(x=10, y="10")   # validation error
print(obj)
# print(obj1)

print(obj.model_dump())         # {'x': 10, 'y': 20} (dict)
print(obj.model_dump_json())    # {"x":10,"y":20} (json/str)

obj2 = A.model_validate({'x':1, 'y': 20 }) # returns A object if validated

print(obj2) # x=1 y=20 has inbuilt __str__ method
print(obj2)

