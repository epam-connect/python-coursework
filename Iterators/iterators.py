class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):                 # not an iterator but behaves same in while loop
        if self.start >= self.end:       # for loop enforces the object to be an iterator
            raise StopIteration
        
        cur = self.start
        self.start += 1
        return cur
    

a = MyRange(1, 10)

# while True:
#     try:
#         print(next(a))
#     except StopIteration as e:
#         break

# for n in MyRange(1, 10):
#     print(next(n))

for i in a:
    print(i)