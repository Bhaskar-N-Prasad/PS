# n = int(input("Enter size of array"))
# l = []
# for i in range(n):
#     l.append(int(input("Enter values")))
# print(l)


# for i in l:
#     if i % 2 == 0:
#         print(i)

# for i in range(len(l)):
#     if i % 2 == 0:
#         print(l[i])

# l = [10,30,8,6,60,90,18,45]
# sum = 0
# for i in l:
#     sum += i
# print(sum/len(l))

def minnn(arr):
    minn = l[0]
    for i in arr:
        if i < minn:
            minn = i
    return minn
l = [90000,90000,100,30,8,6,110,18,45,120,1222]
maxi = l[0]
for i in l:
    if i > maxi:
        maxi = i
print(maxi)
i = 0
sm = minnn(l)
print(sm)
for i in l:
    if i > sm and i != maxi:
        sm = i
print(sm)
