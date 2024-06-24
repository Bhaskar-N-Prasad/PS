# rows = 4
# for i in range(1,rows+1):
#     b=rows-1
#     a = 0
#     for j in range(rows-i):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         s = i+a
#         print(s,end=' ')
#         a = a + b
#         b-=1
#     print()

### Others
## 1->
# rows = 5
# s = 1
# for i in range(1,rows-1):
#     for j in range(rows-i):
#         print(" ",end=" ")
#     temp = s
#     for j in range(1,i+1):
#         print(s,end=" ")
#         s += rows-j
#     s = temp+ 1
#     print()


##2->
# n = 4
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(i,end=" ")
#         i = (i+n-k)
#     print()

rows = 5
for i in range(1,rows+1):
    k = i
    for j in range(rows-i):
        print(" ",end=" ")
    # for j in range(i):
    for j in range(1,i+1):
        print(k,end=" ")
        # k+= rows-1-j
        k+= rows-j
    print()