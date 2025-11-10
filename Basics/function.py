
def fun1(*args, **kwargs):
    # print(args, kwargs)
    print([*kwargs])

# fun(1,2,3,4,5)

a = list(map(lambda x : x * 2, [1,2,3,4]))

def fun(*args, **kargs):
    fun1(*args, **kargs)


a = (1,2,3,4)
b = [*a]
# print(b)

fun(1, 2, 3, 4, c=10, d=10)