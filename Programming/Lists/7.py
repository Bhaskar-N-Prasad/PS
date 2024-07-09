# x = [10,20,10,30,40,20,20]
# count = 0
# def dup(x):
#     y = []
#     if len(x) == 0 or len(x) == 1:
#         return x
#     for i in x:
#         if i not in y:
#             y.append(i)
#     return y

# print(dup(x))


x = [10,20,10,30,40,20,20]
def occurence(x,num):
    dict = {}
    for i in x:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for i in dict:
        print(i," ",dict[i])
    if num in dict:
        return dict[num]
    else:
        return 0

print(occurence(x,20))