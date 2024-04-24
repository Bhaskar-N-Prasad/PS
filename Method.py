########### NO parameter no return value #########
class Calculator:
    def __init__(self):
        self.a = 10
        self.b = 20
    def display(self):
        x = 100
        y = 200
        r1 = x + y
        print(r1)
c1 = Calculator()
print(c1.a)
print(c1.b)
c1.display()

############### No parameter but return value #########

class Calculator2:
    def __init__(self):
        self.a = 10
        self.b = 20
    def display(self):
        x = 100
        y = 200
        r1 = x + y
        return r1
c1 = Calculator2()
print(c1.a)
print(c1.b)
s = c1.display()
print(s)
