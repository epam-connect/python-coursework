a = [5, 2, 4 ,6, 9]
prefix = []

for i in a:
    prefix.append(i * prefix[-1] if prefix else i)

# print(prefix)
# print(prefix[-1] // prefix[2])