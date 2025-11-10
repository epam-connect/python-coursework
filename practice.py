# class MyClass:
#     def __init__(self, a, b):
#         self.a, self.b = a, b
    
#     def __add__(self, other):
#         return MyClass(self.a + other.a, self.b + other.b)

#     def __gt__(self, other):
#         return self.a > other.a or (self.a == other.a and self.b > other.b)
    
#     def __repr__(self):
#         return f"{self.a}, {self.b}"

#     def __getitem__(self, key):
#         return self.key
    
#     def __setitem__(self, key, val):
#         self.key = val

# obj1 = MyClass(2, 6)

# obj2 = MyClass(2, 5)
# obj1["item"] = "new item"

# print(obj1["item"])
# print(obj1 > obj2)
    
    
class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self): #Must return an iterable
        return Iterator_MyRange(self)


class Iterator_MyRange:
    def __init__(self, val):
        self.start = val.start
        self.end = val.end

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration()
        val = self.start
        self.start += 1
        return val

obj = MyRange(1, 10)
iter = iter(obj)

for i in iter:
    print(i)        
