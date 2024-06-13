class Plane():
    # def takeoff(self):
    #     print("Plane takeoff")
    def fly(self):
        print("Plane flying")
    def land(self):
        print("Plane is flying")
class Cargoplane(Plane):
    def takeoff(self):
        print("Cargo is taking off")
    def fly(self):
        print("Cargo is flying")
    def land(self):
        print("Cargo is landing")
    def carryc(self):
        print("Cargo is carrying goods")
class Passengerplane(Plane):
    def takeoff(self):
        print("PassengerPlane is taking off")
    def fly(self):
        print("PassengerPlane is flying")
    def land(self):
        print("PassengerPlane is landing")
    def carryc(self):
        print("PassengerPlane is carrying Passenger")
class Fighterplane():
    def takeoff(self):
        print("FighterPlane is taking off")
    def fly(self):
        print("FighterPlane is flying")
    def land(self):
        print("FighterPlane is landing")
c = Cargoplane()
p = Passengerplane()
f = Fighterplane()
def allowPlane(ref):
    ref.takeoff()
    ref.fly()
    ref.land()
print(id(c.takeoff))
print(id(p.takeoff))
print(id(f.takeoff))

allowPlane(c)
allowPlane(p)
allowPlane(f)
# P = Plane()