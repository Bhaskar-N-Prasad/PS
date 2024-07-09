l1 = [0,0,0,0]
l2 =[1,"jaj",1]

a = [10,20,30,40]
print(all(a))
print(any(a))
print(all(l1))
print(any(l1))
print(all(l2))
print(a.extend(l2))
print(a)
# print(sorted(a))

print(a.append(l2))
print(a)
a.pop()
print(a.index(1))



