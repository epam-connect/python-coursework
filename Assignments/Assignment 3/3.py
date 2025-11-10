def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
        yield fact

num = 5

for value in  factorial(5):
    print(value)

print(f"Factorial of {num} is {value}")