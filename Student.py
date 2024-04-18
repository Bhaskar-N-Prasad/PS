class Student:
    def __init__(self):
        self.name = "Rama"
        self.age = 21
        self.height = 5.8
        self.addr = "Bengaluru"
    def eat(self):
        print("Student is eating")
    def study(self):
        print("Student is studying")
s1 = Student()
print(s1.name)
print(s1.age)
print(s1.height)
print(s1.addr)
s1.eat()
s1.study()

