#Create function accepts arbitrary number of keyword arguments and return dictionary with keys and values swapped as shown below

def get_reversed(**kwargs):
    print(kwargs)
    return { val : key for key, val in kwargs.items() }

print(get_reversed(a=1, b=2, c=3))