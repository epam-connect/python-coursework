class A:
    a = 10
    def __init__(self):
        print("A")
    def fun(self):
        print("fun from A")
    
class B(A):
    a = 20
    def __init__(self):
        print("B")
        super().__init__()
    
    def fun(self):
        print("fun from B")
    
    def getA(self):
        return super().a
    

obj = B()

print(obj.getA())