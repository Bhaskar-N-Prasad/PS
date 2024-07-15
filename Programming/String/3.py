# rows = 5
# for i in range(rows):
#     for j in range(rows-i):
#         print(' ',end=' ')
#     for j in range(i+1):
#         print('*',end=' ')
#     for j in range(i):
#         print('*',end=' ')
#     print()

s = 'ABDEF'
def rev(str):
    newstr = ''
    for i in str:
        newstr = i + newstr
    return newstr
res = rev(s)
for i in res:
    print(chr(ord(i)+1),end='')
