#Write a program that accepts a sentence and calculate the 
#number of upper-case letters and lower-case letters.

val = input("Enter any text : ")
upper_count, lower_count = 0, 0

for ch in val:
    if ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1

print("UPPER CASE", upper_count)
print("LOWER CASE", lower_count)
