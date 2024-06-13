class Os:
    def __init__(self):
        self.status = True
        print("Os is installing")
    def getOs(self):
        print("OS is still waiting")
class Mobile:
    def __init__(self,name):
        self.mname = name
        self.o = Os()
        print("Mobile is Ready")
        print("with OS Installed")
m = Mobile("iphone")
print(m.mname)
print(m.o.status)
m.o.getOs()
del m
print("After del m")
print(m.mname)
print(m.o.status)