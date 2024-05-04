data = input("Enter a string")
# x = data.split()
# print(len(x))
# res = []
# for i in range(len(x)-1,-1,-1):
#     print(x[i])
#     res.append(x[i])
# print(res)
# print("".join(res))

str = ""
for i in range(len(data)-1,-1,-1):
    str += data[i]
print(str)