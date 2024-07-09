
def merge(a,b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if a:
        while i < len(a):
            c.append(a[i])
            i += 1
    if b:
        while j < len(b):
            c.append(b[j])
            j += 1
    return c
def divide(l):
    if len(l) == 1:
        return l
    mid = len(l)// 2
    left = l[:mid]
    right = l[mid:]
    sl = divide(left)
    sr = divide(right)
    return merge(sl,sr)
 
l = [12,24,5,6,8,23,11]
res = divide(l)
print(res)