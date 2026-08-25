# Bank Application using Dictionary

bank_db = {}

def create_account():
    acc_no = input("Enter Account Number: ")

    if acc_no in bank_db:
        print("Account number already exists!")
        return

    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    bank_db[acc_no] = {
        "name": name,
        "phone": phone,
        "balance": 0
    }

    print("Account created successfully!")


def balance_check():
    acc_no = input("Enter Account Number: ")

    if acc_no in bank_db:
        print("Account Holder:", bank_db[acc_no]["name"])
        print("Balance:", bank_db[acc_no]["balance"])
    else:
        print("Account not found!")


def deposit():
    acc_no = input("Enter Account Number: ")

    if acc_no in bank_db:
        amount = float(input("Enter amount to deposit: "))
        bank_db[acc_no]["balance"] += amount
        print("Amount deposited successfully!")
        print("Updated Balance:", bank_db[acc_no]["balance"])
    else:
        print("Account not found!")


def withdraw():
    acc_no = input("Enter Account Number: ")

    if acc_no in bank_db:
        amount = float(input("Enter amount to withdraw: "))

        if amount > bank_db[acc_no]["balance"]:
            print("Insufficient balance!")
        else:
            bank_db[acc_no]["balance"] -= amount
            print("Withdrawal successful!")
            print("Remaining Balance:", bank_db[acc_no]["balance"])
    else:
        print("Account not found!")


while True:
    print("\n------ BANK APPLICATION ------")
    print("1. Create Account")
    print("2. Balance Check")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_account()
    elif choice == 2:
        balance_check()
    elif choice == 3:
        deposit()
    elif choice == 4:
        withdraw()
    elif choice == 5:
         break
    else:
        print("Invalid choice!")
        print("Thanks")


