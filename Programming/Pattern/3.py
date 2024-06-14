k = 65
rows = int(input("Enter a number"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(chr(k),end=' ')
        k += 1
    print()
# k = 1
# rows = int(input("Enter a number"))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(k,end=' ')
#         k += 1
#     print()
