def count(n):
    for i in range(1, n + 1):
        yield i

# generator = count(10)
# print(next(generator))
# print(next(generator))
# print(next(generator))

for i in count(10):
    print(i)