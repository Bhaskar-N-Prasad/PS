###### Hotel Bill using Conditional Statements #######

idli_rate = 20
dosa_rate = 30
poori_rate = 40

def menu():
    print("1.IDLI\n2.DOSA\n3.POORI\n")
    print("Enter your choice")
    return int(input())

def billoo():
    print("Hotel Name")
    print("GSTIN")
    print("Cash")
    print("------------------")
    print("Bill No\tBill Date\n")
    print("-----------------")
    print("ItemName\tQty\tRate\tAmount")

def bill():
    c = menu()
    total = 0
    if c == 1:
        cost = idli_rate
        gst = idli_rate * 0.12
        print("enter Quantity")
        qty = int(input())
        billoo()
        print(f"Idli\t{qty}\t{idli_rate}\t{qty * idli_rate}")
        print("------------")
        total += (qty * idli_rate) + gst

        print(f"Gst-12%\t\t{idli_rate * 0.12}")
        print(f"total\t\t{total}")
# while True:
#     c = menu()
#     cost = 0
#     if c == 1:
#         cost += 20
#     elif c == 2:
#         cost += 30
#     else:
#         cost += 40
#     if c == 4:
#         break

# print(cost)
bill()