

data = input("Enter a string\n")
str = ""
for i in data:
    if ord(i)>=65 and ord(i)<=90:
        str += chr(ord(i)+32) 
    else:
        str += i
print(str)