def rev(num,res):
    if num == 0:
        return res
    return rev(num//10,(num%10)+(res*10))

num = 123
res = rev(num,0)
print(res)