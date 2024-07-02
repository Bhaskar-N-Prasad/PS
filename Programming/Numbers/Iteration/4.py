def checkPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
num = 2
res = checkPrime(num)
if res == True:
    print("Prime")
else:
    print("Not Prime")