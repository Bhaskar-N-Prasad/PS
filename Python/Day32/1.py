# print("Enter a number")
# a = int(input())
# print('enter value 2')
# b = int(input())
# c = a/b
# print("Result is ",c)
# print("PGM end")
print("Enter a number")
a = int(input())
print('enter value 2')
b = int(input())
try:
    c = a/b
    print("Result is ",c)
except Exception as e:
    print("Error is ",e)
else:
    print("PGM end")