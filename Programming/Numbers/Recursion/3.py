# def factorial(num):
#     if num <=1:
#         return 1
#     return num*factorial(num-1)


# num = 5
# res = factorial(num)
# print(res)

def factorial(num):
    if num ==0:
        return 0
    return factorial(num//10)+1


num =123
res = factorial(num)
print(res)