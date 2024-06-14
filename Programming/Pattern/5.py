y = 0
rows = 5
for i in range(1,rows+1):
    y += i
    temp = y
    for j in range(1,i+1):
        print(temp,end=' ')
        temp -= 1
    print()
'''
1
3 2
6 5 4
10 9 8 7
15 14 13 12 11
'''
