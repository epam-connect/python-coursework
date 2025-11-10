class A:
    class_val = 10

    def change_val(self, val):
        self.class_val = val
    
    @classmethod
    def change_global_val(cls, val):
        cls.class_val = val


obj1 = A()
obj1.class_val += 11
print(obj1.class_val)

obj2 = A()
print(obj2.class_val)
obj3 = A()
print(obj2.class_val)

A.change_global_val(18)

print(obj1.class_val)
print(obj2.class_val)
print(obj3.class_val)