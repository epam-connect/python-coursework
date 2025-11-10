class Descripter:
    def __init__(self, key):
        self.key = key
    
    def __get__(self, instance, owner):
        print(f"Getting {self.key}")    
        return instance.__dict__[self.key]
    
    def __set__(self, instance, value):
        print(f"Setting {self.key} to {value}")
        instance.__dict__[self.key] = value
    
    def __delete__(self, instance):
        print(f"Deleting {self.key}")
        del instance.__dict__[self.key]
    
class MyClass:
    name = Descripter("name")
    email  = Descripter("email")

    def __init__(self, name, email):
        self.name = name
        self.email = email

obj = MyClass("Ankan Debnath", "anakndebnath@gmail.com")
print(obj.name)
obj.name = "New Name"
print(obj.name)

del obj.name

#another syntax
class MyClass1:
    def set_val(self, val):
        if val < 0:
            raise Exception("Value can not be negative")
        print("setting")
        self._val = val
    def get_val(self):
        print("getting")
        return self._val
    def del_val(self):
        print("deleting")
        del self._val
    
    val = property(get_val, set_val, del_val)

class MyClass2:
    def __init__(self):
        self._val = None
    
    @property
    def val(self):
        return self.val

    @val.setter
    def val(self, val):
        print("setting")
        self._val = val
    
    @val.getter
    def val(self):
        print("getting")
        return self._val

    @val.deleter
    def val(self):
        print("deleting")
        del self._val