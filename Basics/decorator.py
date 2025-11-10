
def special_sub(fun):
    def wrapper(*args, **kwargs):
        print("something")
        return fun(*args, **kwargs) 
    return wrapper


@special_sub
def sub(a : int, b : int):
    return a - b

@special_sub
def add(a, b, c):
    return a + b + c

# new_sub = special_sub(sub)
print(sub(1, 10))
print(add(1, 10, 20))


def do_mul(n):
    def decorator(fun):
        def wrapper(name):
            for i in range(n):
                fun(name)
        return wrapper
    return decorator

def decorator(fun):
    def wrapper(name):
        fun(name)
    return wrapper

@do_mul(5)
def greet(name):
    print(name)

greet("Hello")

# do_mul(5)(greet)("Ankan")


# def add(a, b):
#     return a + b

# def decorator(val):
#     def wrapper(x):
#         return add(val, x)
    
#     return wrapper

# add_10 = decorator(10)
# print(add_10(15))