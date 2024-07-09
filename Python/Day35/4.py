# t = ('Rama',[10,20,30])
# print(t)
# name,ia_marks = t
# print(name)
# print(ia_marks)

# names = ['Dhoni','Gayle','Rohith','VK']
# run = [10000,20000,30000,40000]
# country = ['India','WI','India','India']
# ipl_t = ['CSK','Pujab','MI','RCB']
from itertools import zip_longest

names = ['DK','Warner','Jacks','Maxwell']
run = [10000,20000,30000,40000]
country = ['India','Australia','England','Australia']
ipl_t = ['RCB','DC']

x = list(zip_longest(names,run,country,ipl_t,fillvalue='#'))

print(x)

# x = tuple(zip(names,run,country,ipl_t))
# print(x)