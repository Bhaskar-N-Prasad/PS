# t1 = (20,)
# print(type(t1))
#indexing
# t = (10,20,30,"ram",40,50)
# print(t[2])
# print(t[4])
# t2 = ("rama",8,10,"Sita")
# print(t2[:3])
# print(t2[1:3])
# print(t2[-1:-3])
# print(t2[-3:-1])
# print(t2[-1:-3:-1])

#Nested tuple
t = (1,2,3,('Rama','Sita',('Ravana',80)),100,)
print(t[3][0])
print(t[4])
print(t[3][2][0])
print(t[-2][-1][-1])


####### Insertion and Deletion in tuple
t = (10,20,30,[40],50,60)
t2 = t[:2] + (25,) + t[2:]
print(t2)
t3 = t[:3] + t[4:]
print(t3)
