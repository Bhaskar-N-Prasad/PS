s = 'silent hdh '
t = ' listen hdh'
def ana(s,t):
    ana1,ana2 = d(s),d(t)
    print(ana1)
    print(ana2)
    if ana1 == ana2:
        return True
    else:
        return False

def d(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

print(ana(s,t))