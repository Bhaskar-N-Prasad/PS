# num = 1
# count = 0
# for i in range(1,(num)+1):
#     if num % i == 0:
#         count += 1
#         if count >=3 :
#             print("Not Prime")
#             break
# if count == 2:
#     print("Prime")

# def countFac(num):
#     count = 0
#     for i in range(1,num+1):
#         if num % i ==0:
#             count += 1
#     return count
# num = 16
# count = countFac(num)
# if count == 2:
#     print("Prime")
# else:
#     print("Not Prime")


def countFac(num):
    count = 0
    for i in range(1,num+1):
        if num % i ==0:
            count += 1
    return count
for k in range(1,500+1):
    num = k
    count = countFac(num)
    if count == 2:
        print(num)
