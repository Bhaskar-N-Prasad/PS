rows = 5
for i in range(1,rows+1):
    for j in range(rows-i):
        print(' ',end=' ')
    for j in range(rows,rows-i,-1):
        print(j,end=' ')
    for j in range(rows+2-i,rows + 1,1):
        print(j,end=' ')
    print()

rows = 5
for i in range(1,rows+1):
    for j in range(rows-i):
        print(' ',end=' ')
    for j in range(i,0,-1):
        print(j,end=' ')
    for j in range(2,i+1,1):
        print(j,end=' ')
    print()