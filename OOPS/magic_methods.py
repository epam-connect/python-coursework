class myclass:
    def __init__(self, a, b):
        self.a, self.b = a, b
    
    def __str__(self):
        return f'a : {self.a} b : {self.b}'
    
    def __add__(self, other):
        return myclass(self.a + other.a, self.b + other.b)
    
    
obj1 = myclass(10, 15)
print(obj1)

obj2 = myclass(5, 8)
print(obj2)

print(obj1 + obj2)

# a : 10 b : 15
# a : 5 b : 8
# a : 15 b : 23