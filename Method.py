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

#####################    With parameter but no return value    ##########

class Calculator3:
    def __init__(self):
        self.a = 10
        self.b = 20
    def display(self,x,y):
        r1 = x + y
        print(r1)
c1 = Calculator3()
print(c1.a)
print(c1.b)
n1 = 100
n2 = 200
c1.display(n1,n2)

####################### With parameter with return value ##########

class Calculator4:
    def __init__(self):
        self.a = 10
        self.b = 20
    def display(self,x,y):
        r1 = x + y
        return r1
c1 = Calculator4()
print(c1.a)
print(c1.b)
n1 = 100
n2 = 200
s = c1.display(n1,n2)
print(s)


############ ACtual storing in self ##############

class Fan:
    def __init__(self):
        self.brand = "Usha"
        self.color = "Black"
        self.cost = 2500
        print(self)
f1 = Fan()
print(f1)
f2 = f1
print(f2)