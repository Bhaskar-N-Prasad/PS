class Fan:
    def __init__(self):
        self.brand = "Chroma"
        self.color = "Blue"
        self.cost = 15000
        self.numOfBlades = 3
    # def rotate(self):
    #     print("Fan is rotating")
f1 = Fan()
# print(f1.brand)
# print(f1.color)
# print(f1.cost)
# print(f1.numOfBlades)
# f1.rotate()
f2 = f1
print(f1)
print(f2)
print(id(f1))
print(id(f2))
print(f1 is f2)
