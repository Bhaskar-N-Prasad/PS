rows = 5
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(rows+1-j,end=" ")
    for j in range(i-1,0,-1):
        print(rows+1-j,end=" ")
    print()
for i in range(1,rows):
    for j in range(1,i+1):
        print(" ",end=" ")
    for j in range(1,rows-i+1):
        print(rows+1-j,end=" ")
    for j in range(rows-i-1,0,-1):
        print(rows+1-j,end=" ")
    print()