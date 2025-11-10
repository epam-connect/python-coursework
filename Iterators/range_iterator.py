# Seperate Iterable and iterator
class MyRange:                          #Custom rang class
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return MyRangeIterator(self)
    
class MyRangeIterator:                  #MyRange object Iterator
    def __init__(self, obj):
        self.obj = obj
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.obj.start > self.obj.end:
            raise StopIteration
        
        cur = self.obj.start
        self.obj.start += 1
        return cur
                

obj = MyRange(1, 12)

it = iter(obj)

while True:
    try:
        print(next(it))
    except StopIteration as e:
        break