#Create list compreshension for numbers between 1 to 20 whose square are even numbers
a = [  n*n for n in range(1, 21) if n*n % 2 == 0]
print(a)