# for i in range(5):
#     for j in range(5):
#         print(i,end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end=' ')
#     print()

# for i in range(5):
#     for j in range(5):
#         print(j,end=' ')
#     print()
rows = int(input("Enter the number of rows"))
# for i in range(1,rows+1):
#     for j in range(1,rows+1):
#         print(j,end=' ')
#     print()
for i in range(1,rows+1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()