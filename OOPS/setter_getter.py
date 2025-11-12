class myclass:
    def __init__(self):
        self._x = 0
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):         #type checking in setter
        if type(value) is not int:
            raise Exception("Type must be int")
        else:
            self._x = value
    
    @x.getter       # getting logic in getter
    def x(self):
        return self._x + 10

# obj = myclass()
# obj.x = 10
# print(obj.x)

class MyClass:
    def set_x(self, x):
        self._x = x
    
    def get_x(self):
        return self._x

    def del_x(self):
        del self._x
    
    property(get_x, set_x, del_x)

obj = MyClass()
print(obj.__dict__)
obj.set_x(10)
print(obj.__dict__)
print(obj.get_x())
print(obj.__dict__)
obj.del_x()