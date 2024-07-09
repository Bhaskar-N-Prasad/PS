l1 = [1,2,3,4,5,6,7]
# del l[1]
# l.remove(4)
# print(l)
# print(l[-1:-8:1])
l = [10,20,[35,40],80,['Sita','ravana',['rama','pentagon']],100]
print(len(l))
print(l[4][2][0])
print(l[4][2][1])
print(l[4][1])
print(l[2][1])
l2= [1,23]

############## Arithmetic operators in list
print(l1*2)
print(l1+l2)
print(2 in l1)
print(2 not in l1)
print(2 not in l2)
print(3 in l2)

print(l1-2)
print(l1/2)