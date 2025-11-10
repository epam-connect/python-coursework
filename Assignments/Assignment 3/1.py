#Create a generator-based method to print even numbers from 0 to 50

def get_numbers(limit):
    for i in range(1, limit + 1):
        yield i

generator = get_numbers(50)

while True:
    try:
        print(next(generator))
    except StopIteration as err:
        print("Finished")
        break

#for loop handles the above exception handling by default
for num in get_numbers(50):
    print(num)