class Radio:
    def turnOn(self,x):
        if x == 1:
            print("Radio is on")
        else:
            print("Radio is off")
class Car:
    def __init__(self,min,max):
        self.cmin = min
        self.cmax = max
        self.r = Radio()
c1 = Car(80,60)
print(c1.cmin)
print(c1.cmax)
c1.r.turnOn(1)
c1.r.turnOn(0)