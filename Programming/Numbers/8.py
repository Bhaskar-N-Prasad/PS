num = 1634

def countDigit(num):
    count = 0
    while num != 0:
        num //= 10
        count += 1
    return count

dig = countDigit(num)
print(dig)
def arm(num):
    res = 0
    while num != 0:
        rem = num % 10
        res += rem ** dig
        num //= 10
    return res
if arm(num) == num:
    print("Armstrong Number")
else:
    print("Not")