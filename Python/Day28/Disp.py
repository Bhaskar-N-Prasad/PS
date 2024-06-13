class O:
    def disp(self):
        print("O")
class A(O):
    def disp(self):
        print("A")
class B(O):
    def disp(self):
        print("B")

class C(A):
    def disp(self):
        print("C")
class D(A,B):
    def disp(self):
        print("D")
class E(B):
    def disp(self):
        print("E")
class F(C,D):
    def disp(self):
        print("F")
        super().disp()
class G(D,E):
    def disp(self):
        print("F")
class H(F,G):
    def disp(self):
        print("H")
f = H()
print(H.mro())
print(F.mro())
print(G.mro())
f.disp()
