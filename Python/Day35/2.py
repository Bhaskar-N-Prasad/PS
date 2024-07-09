l = [10,20,30,40]
l.insert(1,25)
l.append(35)
print(l)
l.extend([50,60])
print(l)
l.pop()
print(l)
l.clear()
print(l)
del l
# print(l)
l = [10,20,10,40,50]
print(l.count(10))
print(l.index(10))

x = [10,20,5]
new = [i for i in x if i % 2 == 0]
print(new)