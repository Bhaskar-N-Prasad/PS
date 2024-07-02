def binSearch(list,key):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high)//2
        if list[mid] == key:
            return mid
        elif list[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

l = [1,2,3,4,5,6,7,8,9,10]
key = 8
print(binSearch(l,key))