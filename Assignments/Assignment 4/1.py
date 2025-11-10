#Create a class with public, private and protected methods, create 2 instances and compare if ‘id’ of instances are same

class MyClass:
    def fun_public(self):
        print("Public method")

    def _fun_protected(self):
        print("Protected method")
    
    def __fun_private(self):
        print("This is private method")


obj1 = MyClass()
obj2 = MyClass()

obj1.fun_public()
obj1._fun_protected()
# obj1.__fun_private() -> AttributeError

print(id(obj1))
print(id(obj2))