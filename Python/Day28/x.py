class z1():
    pass
class z2(z1):
    pass
class z3(z1):
    pass
class z4(z1):
    pass
class z5(z1):
    pass
class k1(z2):
    pass
class k2(z2,z3):
    pass
class k3(z3,z4):
    pass
class k4(z4,z5):
    pass
class k5(z5):
    pass
class m1(k1,k2):
    pass
class m2(k3,k4):
    pass
class m3(k4,k5):
    pass
class y1(m1,m2):
    pass
class y2(m2,m3):
    pass
class k(y1,y2):
    pass
print(k.mro())
print("z1",z1.mro())
print("z2",z2.mro())
print("z3",z3.mro())
print("z4",z4.mro())
print("z5",z5.mro())
print("k1",k1.mro())
print("k2",k2.mro())
print("k3",k3.mro())
print("k4",k4.mro())
print("k5",k5.mro())
print("m1",m1.mro())
print("m2",m2.mro())
print("m3",m3.mro())
print("y1",y1.mro())
print("y2",y2.mro())
