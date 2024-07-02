# a = 12
# b = 20
# if a < b:
#     sml =  a
# else:
#     sml = b
# for i in range(sml+1,0,-1):
#     if a%i == 0 and b%i == 0:
#         hcf = i
#         break
# print(hcf)

#LCM

a = 11
b = 13
if a < b:
    lar = b
else:
    lar = a
for i in range(lar,a*b+1):
    if i%a == 0 and i%b == 0:
        lcm = i
        break
print(lcm)