def fun(n):
    for i in range(1, n + 1):
        yield i

generator = fun(10)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# import function

# print(__name__)