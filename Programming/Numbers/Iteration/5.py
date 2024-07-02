#perfect number
# def pf(num):
#     sum = 0
#     for i in range(1,num):
#         if num % i == 0:
#             sum += i
#     if sum == num:
#         print("Perfect Number")
#     else:
#         print("Not Perfect Number")
# pf(12)

# def pf(num):
#     for i in range(1,num+1):
#         sum = 0
#         for j in range(1,i):
#             if i % j == 0:
#                 sum += j
#         if sum == i:
#             print(i)
# pf(10000)

def perfect(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum += i
    return sum

for i in range(1,10000):
    if perfect(i) == i:
        print(i)

