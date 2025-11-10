#Write a program that accepts a sequence of whitespace separated words as input 
# and prints the words after removing all duplicate words and sorting them alphanumerically.

val = input("Enter comma-seperated numbers : ")
words = val.split(' ')

words = list(set(words))
words.sort()

print(words)