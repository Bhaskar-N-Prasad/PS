s = 'rama is running rama is sleeping hi rama'
word = 'rama'
k = s.split()
c = 0
for i in k:
    if i.lower() == word.lower():
        c += 1
print(c)