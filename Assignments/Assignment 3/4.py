
class MyDecorator:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        try:
            return self.func(*args, **kwargs)
        
        except ZeroDivisionError as err:
            return "Zero division error"



def func_decorator(func):
    def wrapper(number1, number2):
        try: 
            return func(number1, number2)
        except ZeroDivisionError:
            return "Zero division error"
    
    return wrapper


# @MyDecorator                # div = MyDecorator(div).__call__
# @func_decorator
def div(number1, number2):
    return number1 / number2



print(div(1, 0))