class BankAccount:
    def __init__(self, name, account_num, balance):
        self.name = name
        self.account_num = account_num
        self.__balance = balance
        self.transaction_list = []

    def check_balance(self):
        print(f"Current balance: ₹{self.__balance}")

    def deposit(self):
        amount = int(input("Enter depositing amount here: ₹"))
        if amount <= 0:
            print("Please deposit a positive amount!")
        else:
            self.__balance += amount
            self.transaction_list.append(f"Deposited: ₹{amount} || Balance: ₹{self.__balance}")
            print(f"Deposited amount: ₹{amount}")
            print(f"Balance after deposit: ₹{self.__balance}")
            
    def withdraw(self):
        amount = int(input("Enter withdrawing amount here: ₹"))
        if amount <= 0:
            print("Please withdraw a positive amount!")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            self.transaction_list.append(f"Withdrawn: ₹{amount} || Balance: {self.__balance}")
            print(f"Withdrew amount: ₹{amount}")
            print(f"Balance after withdraw: ₹{self.__balance}")

    def transaction_history(self):
        print("\n=========Transaction history==========\n")
        for transaction in self.transaction_list:
            print(transaction)

        print("")

    def transfer(self, accounts):
        try:
            account_num = int(input("Enter the account number you want to transfer money into: "))
            amount = int(input("Enter the amount you want to transfer: ₹"))

            account2 = next(
                (account for account in accounts if account.account_num == account_num),
                None
            )

            if account2 is None:
                print("Destination account doesn't exist!")
            elif account2 is self:
                print("You cannot transfer money to the same account!")
            elif amount <= 0:
                print("Please transfer a positive amount!")
            elif amount > self.__balance:
                print("Insufficient balance!")
            else:
                self.__balance -= amount
                account2.__balance += amount
                print(f"Transferred ₹{amount} to account {account2.account_num}")
                self.transaction_list.append(f"Debited: ₹{amount} || Balance: ₹{self.__balance}")
                account2.transaction_list.append(f"Credited: ₹{amount} || Balance: ₹{account2.__balance}")
        except ValueError:
            print("Please enter valid whole numbers for the account number and amount!")

class Menu:
    def __init__(self):
        self.accounts = []

    def start(self):
        while True:
            print("""
========== BANK SYSTEM ==========

1. Sign up
2. Login
3. Exit
""")
            self.choice = input("Enter your choice: ")

            if self.choice == "1":
                self.signup()

            elif self.choice == "2":
                self.login()

            elif self.choice == "3":
                quit()

    def signup(self):
        name = input("Name: ")
        account_num = int(input("Enter account number: "))
        balance = int(input("Enter balance: ₹"))

        account = BankAccount(name, account_num, balance)
        print("\nSignup successfull!")
        self.__add_account(account)
        return

    def login(self):
        account_num = int(input("Enter account number to login: "))
        for account in self.accounts:
            if account.account_num != account_num:
                continue

            print("\nYou're logged in!")

            while True:
                print(f"""
========== WELCOME {account.name.upper()} ==========

1. Check balance
2. Deposit
3. Withdraw
4. Transfer
5. Transaction history
6. Logout
""")
                self.choice = input("Enter your choice: ")

                if self.choice == "1":
                    account.check_balance()

                elif self.choice == "2":
                    account.deposit()

                elif self.choice == "3":
                    account.withdraw()

                elif self.choice == "4":
                    account.transfer(self.accounts)

                elif self.choice == "5":
                    account.transaction_history()

                elif self.choice == "6":
                    return

        print("\nAccount doesn't exist!")

    def __add_account(self, account):
        if account not in self.accounts:
            self.accounts.append(account)

        else:
            print("Account already exists")

    def remove_account(self, account):
        if account not in self.accounts:
            print("Account doesn't exist")

        else:
            self.accounts.remove(account)

    
menu = Menu()
menu.start()