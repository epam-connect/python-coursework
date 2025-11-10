def fun(a, b):
    print(a, b)

def call_fun(kwargs):
    fun(**kwargs)

call_fun({'a' : 10, 'b' : 20})