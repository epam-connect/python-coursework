class X:
    def __new__(cls):
        # print(cls)
        print(f"Creating instance of {cls.__name__} in X")
        instance = super(X, cls).__new__(cls)  # Calls object.__new__(cls)
        # print(instance)
        print(f"Returning instance from X")
        return instance

class Y:
    def __new__(cls):
        # print(cls)
        print(f"Creating instance of {cls.__name__} in Y")
        instance = super(Y, cls).__new__(cls)  # Calls object.__new__(cls)
        # print(instance)
        print(f"Returning instance from Y")
        return instance

class Z(X, Y):  # Multiple inheritance: Z inherits from X and Y
    def __new__(cls):
        # print(cls)
        print(f"Creating instance of {cls.__name__} in Z")
        instance = super(Z, cls).__new__(cls)  # Calls X.__new__() (MRO applies)
        # print(instance)
        print(f"Returning instance from Z")
        return instance
    
'''
super(currentClass, cls)
currentClass: start looking after this class in MRO
cls : which class's MRO to use
'''    

# Creating an instance of Z
print(Z.mro())
obj = Z()