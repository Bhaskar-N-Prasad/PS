def sumOfDigit(num):
    res = 0
    while num!=0:
        rem = num % 10
        res += rem
        num = num // 10
    return res
# print(sumOfDigit(19))
def nextInt(num):
    res = sumOfDigit(num)
    print(res)
    for i in range(100000):
        if sumOfDigit(i) >= 2*res:
            if i > num:
                return i

x = nextInt(499)
print(x)