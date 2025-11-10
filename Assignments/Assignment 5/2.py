#Create a custom exception class which takes a string message as attribute
class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)
    
a = -1

try:
    if a < 0:
        raise MyException("Value cannot be less than 0")
    print("Works fine")

except MyException as e:
    print(e)

