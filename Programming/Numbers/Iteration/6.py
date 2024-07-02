# num = 10110
# res = 0
# while num!=0:
#     rem = num % 10
#     res = (res*10) + rem
#     num = num // 10
# print(res)

def rev(num):
    res = 0
    while num!=0:
        rem = num % 10
        res = (res*10) + rem
        num = num // 10
    return res
num = 1001

for i in range(1,1002):
    res = rev(i)
    if res == i:
        print(res)
# else:
#     print("not pali")