class A:
    def display(self):
        print("Class A")
class B(A):
    def display(self):
        print("Inside B")
class C(A):
    def display(self):
        print("Inside C")
class D(C):
    def displayd(self):
        A.display(self)
        B.display(self)
        C.display(self)
d1 = D()
d1.displayd()