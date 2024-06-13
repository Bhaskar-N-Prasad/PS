class Charger:
    def __init__(self,name):
        self.cname = name
        print("Charger is Ready")
    def getCharger(self):
        print("Charger is not connected")
class Mobile:
    def __init__(self,name):
        self.mname = name
        self.c1 = ""
        print("Mobile is Ready")
    def hasMobile(self,c):
        self.c1 = c
        print("Mobile is Connected")
m = Mobile("iphone")
charge = Charger("iphone charger")
m.hasMobile(charge)
print(m.mname)
print(m.c1.cname)
m.c1.getCharger()
del m
print("After del m")
print(charge.cname)
charge.getCharger()