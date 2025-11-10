from typing import List

class myclass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def print(self):
        print(self.a, self.b)
    
    def __str__(self):
        return f'{self.a} {self.b}'

def add(a, b):
    return a + b

# a = ("Ankan", "Hello", "Ankan")
# print(list(a))

# import sys
# print(sys.executable)

def fun(arg1, arg2):
    '''
        Login
        arg1 : list
        arg2 : int
    '''
    pass

# print(fun)

x : List [int] = ['ankan', 2, 3]
print(x)