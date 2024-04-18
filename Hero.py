######### Memory Management ##############

# 1. Heap Memory
# 2. Stack Memory
# 3. Static Memory
# 4. Code Memory


class Hero:
    def __init__(self):
        self.name = "Yash"
        self.age = 21
        self.height = 5.8
        self.addr = "Bengaluru"
    def act(self):
        print("Hero is acting")
    def dance(self):
        print("Hero is dancing")
h1 = Hero()
# print(h1.name)
# print(h1.age)
# print(h1.height)
# print(h1.addr)
h1.height = 6.0
print(h1.height)
h2 = h1
h3 = h2
print(h3.height)
h1.mob = "89483843342"
print(h2.mob)
print(h3)
print(h2)
h2.act()
h3.dance()


a = 5
print(type(a))
