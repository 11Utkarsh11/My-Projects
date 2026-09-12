account_num = 1000

def home_page(account_num):
    print("""
==================================================
                 🏦 BANK SYSTEM
==================================================

1. Create Account
2. Login
3. Exit
""")
    choice = input("Enter your choice: ")

    if choice == "1":
        create_account(account_num)

    elif choice == "2":
        login()

    elif choice == "3":
        quit()

    else:
        print("Invalid input!")
    
def create_account(account_num):
    name = input("Name: ")
    account_num += 1
    print(f"Account number: {account_num}")
    pin = input("PIN: ")
    print(f"Account number {account_num} successfully created!")


def login():
    pass

def exit():
    pass

# ==================================================
#                   Logged In
# ==================================================

def welcome():
    pass

def check_balance():
    pass

def deposit_money():
    pass

def withdraw_money():
    pass

def transfer_money():
    pass

def transaction_history():
    pass

def logout():
    pass

home_page(account_num)