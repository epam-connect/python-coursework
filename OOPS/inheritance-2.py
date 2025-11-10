class A:
    a = 10
    def __init__(self):
        print("A")
    def fun(self):
        print("fun from A")
    def getA(self):
        return self.a
    
class B:
    a = 20
    def __init__(self):
        print("B")
    
    def fun(self):
        print("fun from B")
    
    def getA(self):
        return self.a
    
class C(B, A):
    def __init__(self):
        super().__init__()
    def getA(self):
        return super().a

obj = C()
print(C.mro())          # B, A, object
obj.fun()               # fun from B
print(obj.getA())       # 20