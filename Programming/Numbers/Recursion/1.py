# def countDigit(num):
#     count = 0
#     while num != 0:
#         num //= 10
#         count += 1
#     return count

def countDigit(num,count):
    if num == 0:
        return count
    return countDigit(num//10,count+1)

def arm(num,res,digit):
    if num == 0:
        return res
    return arm(num//10,((num%10)**digit)+res,digit)


num = 153
digit = countDigit(num,0)
res = arm(num,0,digit)
if res == num:
    print("Armstrong")
else:
    print("Not Armstrong")