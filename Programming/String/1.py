str = 'malayalam'
def rev(str):
    newstr = ''
    for i in str:
        newstr = i + newstr
    return newstr
res = rev(str)
print(res)
if res == str:
    print('palindrome')
else:
    print('not palindrome')