#Create function to take arbitrary number of integer and return the average of those numbers

def get_average(*args):
    return sum(args) / len(args)

print(get_average(1,2,4,5,6))