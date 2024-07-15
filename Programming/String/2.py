vow = "aeiouAEIOU"
def checkV(s):
    v = 0
    c = 0
    w = 0
    for i in s:
        if i in vow:
            v += 1
        elif i == ' ':
            w += 1
        else:
            c += 1
    return [v,c,w]

s = 'hello  bhaskr'
print(checkV(s))