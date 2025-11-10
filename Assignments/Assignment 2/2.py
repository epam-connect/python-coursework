#Use map() to get True for each value greater than 10 in a list of integers, else False
nums = [1,2,34,2,56]
nums_map = list(map(lambda n : True if n > 10 else False, nums))

print(nums_map)