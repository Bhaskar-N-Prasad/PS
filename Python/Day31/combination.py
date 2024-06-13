class Heart:
    def __init__(self,name):
        self.name = name
        print("Heart is Ready")
    def pumping(self):
        print("Heart is Pumping")
class Car:
    def __init__(self,name):
        self.name = name
        print("Car is Ready")
    def driving(self):
        print("Bhaskar is Driving a car")
class Person:
    def __init__(self,name):
        self.name = name
        self.c1 = ""
        self.h = Heart("heart")
        print("Bhaskar is Ready")
    def hasCar(self,c):
        self.c1 = c
        print("Bhaskar has a car")
    def work(self):
        print("Bhaskar is Working")
c = Car("Mustang")
p = Person("Bhaskar")
p.work()
p.hasCar(c)
p.c1.driving()
p.h.pumping()
del p
print("After del p")
print(c.name)
print(p.h.name)