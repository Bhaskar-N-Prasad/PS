# num = 135

def countDigit(num):
    count = 0
    while num != 0:
        num //= 10
        count += 1
    return count


def arm(num):
    dig = countDigit(num)
    res = 0
    while num != 0:
        rem = num % 10
        res += rem ** dig
        num //= 10
    return res

# else:
#     print("Not")


# res = arm(num)
# if res == num:
#     print("Armstrong")
# else:
#     print("Not Armstrong")

for i in range(1,10001):
    if arm(i) == i:
        print(i)