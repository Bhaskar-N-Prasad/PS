from abc import ABC, abstractmethod


# To achieve abstraction we import class called ABC from abc and abstractmethod from abc . 
#IF we add a decorator and extend to base class we can achieve abstraction. Here the object of base class cannot be created.
# The abstract methods in the base class should be overridden by child class.
class Plane(ABC):
    @abstractmethod
    def takeoff(self):
        pass
    @abstractmethod
    def fly(self):
        pass
    # @abstractmethod
    def land(self):
        print("Plane is flying")
class Cargoplane(Plane):
    def takeoff(self):
        print("Cargo is taking off")
    def fly(self):
        print("Cargo is flying")
    # def land(self):
    #     print("Cargo is landing")
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
class Fighterplane(Plane):
    def takeoff(self):
        print("FighterPlane is taking off")
    def fly(self):
        print("FighterPlane is flying")
    def land(self):
        print("FighterPlane is landing")
    def carryc(self):
        print("FighterPlane is carrying Weapons")
c = Cargoplane()
p = Passengerplane()
f = Fighterplane()
def allowPlane(ref):
    ref.takeoff()
    ref.fly()
    ref.land()
    # print(id(ref.takeoff))
allowPlane(c)
allowPlane(p)
allowPlane(f)
# P = Plane()