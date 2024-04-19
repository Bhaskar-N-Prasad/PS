a = int(input("Enter Value 1\n"))
b = int(input("Enter Value 2\n"))
c = int(input("Enter Value 2\n"))
if a > b:
    if a > c:
        print("a is greater than b and c")
elif a < b and a < c:
    print("a is less than b and c")
if b > a and b > c:
    print("b is greater than a and c")
elif b < a and b < c:
    print("b is less than a and c")
if c > a and c > b:
    print("c is greater than a and b")
else:
    print("c is less than a and b")