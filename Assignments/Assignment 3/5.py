#We have a list of mobile numbers. We need to sort those numbers in ascending order 
# and then we need to print them in the standard format of (+91 xxxx xxx xxx). 
# Create a function which performs sorting on mobile numbers and create a decorator which will convert these mobiles into standard format.

def sort_nums(func):
    print("Executing sort_nums")
    def wrapper(nums):
        nums.sort()
        func(nums)
    return wrapper

def add_prefix(func):
    print("Executing add_prefix")
    def wrapper(nums):
        nums = list(map(lambda num : "+91 " + str(num), nums))
        func(nums)
    return wrapper

@sort_nums             # print_nums = sort_nums(print_nums)
@add_prefix            #print_nums = add_prefix(print_nums)
def print_nums(nums):       
    print(nums)

nums = ["7895460981", "9711231230", "9711540230"]

print_nums(nums)

