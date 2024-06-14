'''
1
01
010
1010
10101
'''


k=1
rows = int(input("enter a number"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(k%2,end=' ')
        k+=1
    print()
'''
1
01
101
0101
10101
'''

k=1
rows = int(input("enter a number"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print((i+j+1)%2,end=' ')
        k+=1
    print()