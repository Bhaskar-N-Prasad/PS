# l = [-2,-1000,-10,-20,-40,-100,-60000]
# l = [-36,-24,-48,-7,-2,-5]
# fm = l[0]
# sm = min(l)
# for i in l:
#     if i > fm:
#         sm = fm
#         fm = i
#     elif i<fm and i > sm:
#         sm = i
# print(sm)
l = [46,46,7,8,22,26,6,15]
if l[0] > l[1]:
    max1 = l[0]
    max2 = l[1]
else:
    max1 = l[1]
    max2 = l[0]
for i in l:
    if i > max1:
        max2 = max1
        max1 = i
    elif i > max2 and i != max1:
        max2 = i
print(max2)
