# a = "[(alice, 101, 4.5, Great movie!), (bob, 202, 3.0, Decent show), (alice, 303, 5.0, 'Loved the soundtrack!')]"
# a = a.replace(" ", "")
# a = a.strip("[]()")
# a = a.split("),(")


# reviews = []
# print(a)

# for item in a:
#     user_name, media_cred, rating, comment = item.split(",")
#     user_name = user_name.strip("'")
#     media_cred = media_cred.strip("'")
#     rating = rating.strip("'")
#     comment = comment.strip("'")
#     reviews.append(tuple([user_name, media_cred, rating, comment]))

# print(reviews)


# a = []

# try:
#     while True:
#         val = input().split(',')
#         a.append(val)

# except EOFError:
#     pass

# print(a)


# redis_client = redis.StrictRedis(host="localhost", port="6379", db=0, decode_responses=True)

# class MyDecorate:
#     def __init__(self, fun):
#         self.fun = fun
#     def __call__(self, *args, **kwargs):
#         print("applied logic")
#         return self.fun(*args, **kwargs)
        
# @MyDecorate
# def fun():
#     print("this is fun")

# fun()

def greet_multiple_times(n):
    def decorator(fun):
        def wrapper(*args, **kwargs):
            for i in range(n):
                fun(*args, **kwargs)
        return wrapper
    return decorator

@greet_multiple_times(5)
def greet(name):
    print("Hello ", name)


greet("Ankan")