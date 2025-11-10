from itertools import count

sequence = count(start=1, step=1)
number = next(sequence)

# while number <= 10:
#     print(number)
#     number = next(sequence)

for i in sequence:
    print(i)