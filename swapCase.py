# str = input("Enter a string\n")
# str1 = str.upper()
# str2 = str.lower()
# str3 = str.swapcase()
# print(str)
# print(str1)
# print(str2)
# print(str3)


str1 = "Rama"
str2 = "Sita"
# print(str1 + str2)
# print(str1 - str2)
# print(str1 * str2)
# print(str1 * 3)
# print(str1 / str2)


############String Interning#####

str1 = "Rama"
str2 = "Sita"
str3 = "Ravana"
str4 = "Rama"
str5 = "Rama"
str6 = "Sita"
str7 = "Ravana"

print(id(str1))
print(id(str4))
print(id(str5))
print(id(str2))
print(id(str6))
print(id(str3))
print(id(str7))