#Handling Specific exception

try:
    print("Enter a number")
    a = int(input())
    print("Enter another number")
    b = int(input())
    res = a/b
    print(res)
except ValueError as e:
    print("value Error")
except ZeroDivisionError as e:
    print("Zero Division Error")
except Exception as e:
    print("error")
else:
    print("pgm end")