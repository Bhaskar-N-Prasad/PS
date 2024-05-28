account_b = 1000

def atm_menu():
    print("ATM Menu:")
    print("1. Check b")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")
    return int(input("Please select an option (1-4): "))

def check_b(b):
    print(f"\nYour current b is: Rs{b}")

def withdraw_money(b):
    withdrawal_amount = int(input("\nEnter amount to withdraw: Rs"))
    if withdrawal_amount > b:
        print("Insufficient moneyyy")
    elif withdrawal_amount <= 0:
        print("Invalid amount. Please try again.")
    else:
        b -= withdrawal_amount
        print(f"Withdrawal successfusdl. New b is: Rs{b}")
    return b

def deposit_money(b):
    deposit_amount = int(input("\nEnter amount to deposit: Rs"))
    if deposit_amount <= 0:
        print("Invalid deposit amount. Please try again.")
    else:
        b += deposit_amount
        print(f"Deposit successful. New b is: Rs{b:.2f}")
    return b
while True:
    choice = atm_menu()

    if choice == 1:
        check_b(account_b)

    elif choice == 2:
        account_b = withdraw_money(account_b)

    elif choice == 3:
        account_b = deposit_money(account_b)

    elif choice == 4:
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid ")
