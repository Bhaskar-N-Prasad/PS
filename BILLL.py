print("1.IDLI\n2.DOSA\n3.POORI\n")
print("Enter your choice")
choice = int(input())
total, idli_rate, dosa_rate, poori_rate = 0, 20, 30, 40
cost = 0
if choice == 1:
    cost = idli_rate
    gst = idli_rate * 0.12
    print("Enter Quantity")
    qty = int(input())
    print("\t\tHotel Name")
    print("\t\tGSTIN")
    print("\t\tCash")
    print("--------------------------------------")
    print("Bill No: 1\tBill Date:23-04-2024")
    print("--------------------------------------")
    print("ItemName\tQty\tRate\tAmount")
    print("--------------------------------------")
    print(f"Idli\t\t{qty}\t{idli_rate}\t{qty * idli_rate}")
    print("--------------------------------------")
    total += (qty * idli_rate) + gst
    print(f"Gst-12%\t\t\t\t{idli_rate * 0.12}")
    print(f"total\t\t\t\t{total}")
elif choice == 2:
    cost = dosa_rate
    gst = dosa_rate * 0.12
    print("Enter Quantity")
    qty = int(input())
    print("\t\tHotel Name")
    print("\t\tGSTIN")
    print("\t\tCash")
    print("--------------------------------------")
    print("Bill No:1\tBill Date:23-04-2024")
    print("--------------------------------------")
    print("ItemName\tQty\tRate\tAmount")
    print("--------------------------------------")
    print(f"Idli\t\t{qty}\t{dosa_rate}\t{qty * dosa_rate}")
    print("--------------------------------------")
    total += (qty * dosa_rate) + gst
    print(f"Gst-12%\t\t\t\t{dosa_rate * 0.12}")
    print(f"total\t\t\t\t{total}")
else:
    cost = poori_rate
    gst = poori_rate * 0.12
    print("Enter Quantity")
    qty = int(input())
    print("\t\tHotel Name")
    print("\t\tGSTIN")
    print("\t\tCash")
    print("--------------------------------------")
    print("Bill No:1\tBill Date:23-04-2024")
    print("--------------------------------------")
    print("ItemName\tQty\tRate\tAmount")
    print("--------------------------------------")
    print(f"Idli\t\t{qty}\t{poori_rate}\t{qty * poori_rate}")
    print("--------------------------------------")
    total += (qty * poori_rate) + gst
    print(f"Gst-12%\t\t\t\t{poori_rate * 0.12}")
    print(f"total\t\t\t\t{total}")