#Write a method which accepts a list of numbers and return
#a list containing square of each odd number. Use list comprehension

val = input("Enter comma-seperated numbers : ")
nums = val.split(',')
nums = [ int(n) for n in nums ]

ans = [ n * n for n in nums if n % 2 == 1]

print(ans)