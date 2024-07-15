x = {2,1,3}
print(x)
s1 = {10,20,30,40,50,60}
print(s1)
s = {}
print(type(s))
s2 = set()
print(type(s2))
# print(x[1])
a = set()
for i in range(5):
    data = int(input())
    a.add(data)
print(a)
a.update([60,70])
a.discard(50)
print(a)
a.remove(90)