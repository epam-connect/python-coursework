#Create dictionary with numbers as key and object as list of [square, cube] using comprehension for number as shown below
a = { n : [n**2, n**3] for n in range(1, 21) }
print(a)