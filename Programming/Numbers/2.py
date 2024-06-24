import math

# num = 24
# for i in range(1,(num//2)+1):
#     if num % i == 0:
#         print(i)
# print(num)


# num = 24
# for i in range(1,int(math.sqrt(num))+1):
#     if num % i == 0:
#         print(i)
#         print(num//i)
  

num = 24
for i in range(1,int(math.sqrt(num))+1):
    if num % i == 0:
        print(i)
for i in range(int(math.sqrt(num))+1,0,-1):
    if num % i == 0:
        print(num//i)