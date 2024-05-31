class A:
    def disp(self):
        print("A")
class B(A):
    def disp(self):
        print("B")
class C(A,B):
    def disp(self):
        print("C")
        super().disp()
c = C()
print(C.mro())
c.disp()
