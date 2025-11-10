#Create a Point class with 2 arguments(x,y), and modify ‘str’ function to print in ‘(x,y)’ format. Create 2 instances with different args lets say ob1 and ob2. Modify behaviour of ob1+ob2 to add the values of objects.

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
obj1 = Point(1, 5)
obj2 = Point(2, 7)

print(obj1, obj2)

obj3 = obj1 + obj2 
print(obj3)