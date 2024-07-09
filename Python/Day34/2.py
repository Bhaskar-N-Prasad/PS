l = [10,20,30,[50,60,70],80]
l1 = l.copy()
del l[3][1]
print(l)
print(l1)


##Shallow copy
l = [1,2,3,4]
l1 = l
print(l1)
del l[1]
print(l)
print(l1)


#### Deep copy
l = [1,2,3,4]
l1 = l.copy()
print(l1)
del l[1]
print(l)
print(l1)


import copy

l = [10,20,30,[50,60,70],80]
l1 = copy.copy(l)
del l[3][1]
print(l)
print(l1)


l = [1,2,3,4]
for i,j in enumerate(l):
    print(i," ",j)