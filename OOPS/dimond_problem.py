class A:
    def show(self):
        print("A.show")
class Extra(A):
    pass

class B(Extra, A):
    def show(self):
        print("B.show")
        super().show()  # Calls next in MRO

class C(A):
    def show(self):
        print("C.show")
        super().show()  # Calls next in MRO

class D(B, C):
    def show(self):
        print("D.show")
        super().show()  # Calls next in MRO

d = D()
print(D.mro())          # C3 linearization algorithm
d.show()
