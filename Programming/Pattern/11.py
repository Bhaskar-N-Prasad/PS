rows = 6
cols = 7
for i in range(rows):
    for j in range(cols):
        if(i==1 and j%3==0)or(i==0 and j%3!=0)or (i-j == 2) or (i+j ==8):
            print("*",end=" ")
        elif i==2 and j==2:
            print("R",end=" ")
        elif i==2 and j==3:
            print('C',end=' ')
        elif i==2 and j ==4:
            print('B',end=" ")
        else:
            print(" ",end=" ")
    print()

# rows = 6
# cols = 7
for i in range(1,rows):
    for j in range(cols):
        if(i==4 and j%3==0)or(i==5 and j%3!=0)or (j+i == 3) or (j-i ==3):
            print("*",end=" ")
        elif i==2 and j==2:
            print("R",end=" ")
        elif i==2 and j==3:
            print('C',end=' ')
        elif i==2 and j ==4:
            print('B',end=" ")
        else:
            print(" ",end=" ")
    print()