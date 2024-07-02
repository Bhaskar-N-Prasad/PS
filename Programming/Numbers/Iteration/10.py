def isHappy(n):
    sum = 0
    if n == 1:
        return True
    if n == 4:
        return False
    while n != 0:
        sum += (n % 10) ** 2
        n = n // 10
    return isHappy(sum)
n = 11
print(isHappy(n))


    
# def sumOfDigit(n):
#     r = 0
#     while n != 0:
#         rem = n % 10
#         r = (rem ** 2) + r
#         n = n//10
#     return r

# res = sumOfDigit(19)
# while res != 4 and res != 1:
#     res = sumOfDigit(res)
# for i in range(1,10000):
#     if res == 4:
#         pass
#     else:
#         print(res)