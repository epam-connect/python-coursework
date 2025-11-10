#Write a function my_enumerate that works like enumerate

def my_enumerate(iterable_object, start=0):

    for i in range(len(iterable_object)):
        yield (i + start, iterable_object[i])


nums = [1, 2, 3, 4]

for i, n in my_enumerate(nums):
    print(i, n)