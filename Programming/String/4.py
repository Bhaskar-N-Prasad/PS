def rev(str):
    newstr = ''
    for i in str:
        newstr = i + newstr
    return newstr
s = 'Ronaldo is running'
print(rev(s))
s2 = s.split()
for i in s2:
    print(rev(i),end=' ')
print()

# for i in s:
#     for j in range(len(i)):
#         if j == 0:
#             i[j]=i[j].upper()
# print(s)
    
