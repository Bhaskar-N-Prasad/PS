# rows = 5
# for i in range(rows):
#     for j in range(rows):
#         if i ==0 or j ==0 or i ==rows-1 or j == rows-1:
#             print('*',end=" ")
#         else:
#             print(' ',end=" ")
#     print()

# rows = 5
# for i in range(rows):
#     for j in range(i+1):
#         if i ==0 or j ==0 or i ==rows-1  or i==j:
#             print('*',end=" ")
#         else:
#             print(' ',end=" ")
#     print()

# rows = 11
# for i in range(rows):
#     for j in range(rows):
#         if i ==0 or j ==0 or i ==rows-1 or j == rows-1 or i==j or i ==rows//2 or j ==rows//2 or i + j == rows-1:
#             print('*',end=" ")
#         else:
#             print(' ',end=" ")
#     print()
# rows = 11
# for i in range(rows):
#     for j in range(rows):
#         if i ==0 or j ==0 or i ==rows-1 or j == rows-1  or i ==rows//2 :
#             print('*',end=" ")
#         else:
#             print(' ',end=" ")
#     print()

def printn(num):
    if num == 0:
        print(num)
        return 
    printn(num-1)
    print(num)
    # return "Bhaskar is great haha"
num = 5
res = printn(num)
# print(res)