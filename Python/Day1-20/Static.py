class Farmer:
    r = 2.5
    def  __init__(self,p,t):
        self.p = p
        self.t = t
    def display(self):
        si = (self.p * self.t * Farmer.r) / 100
        print(si)
f1 = Farmer(100000, 2)
f2 = Farmer(200000, 3)
f3 = Farmer(300000, 4)
f1.display()
f2.display()
f3.display()