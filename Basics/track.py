def example_function(pos_arg, *args, default_arg="default", **kwargs):    
    print("Positional argument:", pos_arg)    
    print("args:", args)    
    print("Default argument:", default_arg)    
    print("kwargs:", kwargs)
 
# example_function(10, 20, 30, default_arg="custom", x=1, y=2)

def fibonacci(limit):    
    a, b = 0, 1

    while a < limit:
        yield a
        a, b = b, a + b

gen = fibonacci(2)

print(next(gen))