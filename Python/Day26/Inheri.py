class Parent:
    def __init__(self):
        self.a = 10
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.b = 20
        # super().__init__()
c1 = Child()
print(c1.a)
print(c1.b)