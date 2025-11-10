#Write method which accepts a list of integers nums and 
# an integer result, return indices of the two numbers 
# such that they add up to target


def get_indices(nums, result):
    d = {}

    for i, n in enumerate(nums):
        target = result - n
        
        if target in d:
            return [d[target], i] 

        d[n] = i
    
    return []
    
nums = [2, 7, 11, 15]
result = 9

print(get_indices(nums, result))