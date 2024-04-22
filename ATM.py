
account_balance = 1000.00

def atm_menu():
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")
    return int(input("Please select an option (1-4): "))

def check_balance(balance):
    print(f"\nYour current balance is: ${balance:.2f}")

def withdraw_money(balance):
    withdrawal_amount = float(input("\nEnter amount to withdraw: $"))
    if withdrawal_amount > balance:
        print("Insufficient funds. Please try again.")
    elif withdrawal_amount <= 0:
        print("Invalid withdrawal amount. Please try again.")
    else:
        balance -= withdrawal_amount
        print(f"Withdrawal successful. New balance is: ${balance:.2f}")
    return balance

def deposit_money(balance):
    deposit_amount = float(input("\nEnter amount to deposit: $"))
    if deposit_amount <= 0:
        print("Invalid deposit amount. Please try again.")
    else:
        balance += deposit_amount
        print(f"Deposit successful. New balance is: ${balance:.2f}")
    return balance
while True:
    choice = atm_menu()

    if choice == 1:
        check_balance(account_balance)

    elif choice == 2:
        account_balance = withdraw_money(account_balance)

    elif choice == 3:
        account_balance = deposit_money(account_balance)

    elif choice == 4:
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option (1-4).")
