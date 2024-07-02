def rev(num):
    res = 0
    while num!=0:
        rem = num % 10
        res = (res*10) + rem
        num = num // 10
    return res
rows = 10
k = 1
# r = []
# for i in range(1,1000):
#     if rev(i) == i:
#         r.append(i)
j = 1
for i in range(1,rows+1):
    for j in range(1,i+1):
        # print(k,end=' ')
        # k+=1
        # print(rev(k))
        # print(k)
        # print(r[z],end=' ')
        # z+=1
        while True:
            if rev(k) == k:
                print(rev(k),end=' ')
                break
            else:
                k+=1
        k+=1
    print()

# po = 1

# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         ro = j-1
#         if rev(po)==po:
#             print(po,end=' ')
#         po +=1
#         ro +=1
#         if j == i:
#             j = ro
#     print()
        