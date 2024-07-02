def lSearch(list,key):
    for i in range(len(list)):
        if list[i] == key:
            return i
    return -1

l = [1,2,3,4,5,6,7,8,9,10]
key = 8
print(lSearch(l,key))