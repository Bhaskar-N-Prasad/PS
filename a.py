x = open('names.txt','r')
ptr = x.tell()
print(ptr)
data = x.read(10)
print(data)
ptr2 = x.tell()
print(ptr2)

y = open('x.txt','w')
y.write(data)


x.close()
y.close()