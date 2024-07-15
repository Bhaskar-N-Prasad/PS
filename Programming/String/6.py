def rev(str):
    newstr = ''
    for i in str:
        newstr = i + newstr
    return newstr
s = 'abcb'
res = []
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if rev(s[i:j])== s[i:j]:
            if s[i:j] not in res:
                res.append(s[i:j])
c = 0
pali = ''
for i in res:
    if len(i) > c:
        c = len(i)
        pali = i 
print(pali)




