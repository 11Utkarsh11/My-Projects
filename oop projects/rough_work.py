class BankAccount:
    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.__balance = 0

        if balance > 0:
            self.__balance = int(balance)
        else:
            print("Enter valid balance amount, the amount should be more than 0!")

    def deposit(self, deposit):
        if deposit > 0:
            self.__balance += int(deposit)
        else:
            print("Enter valid deposit amount, the amount should be more than 0!")
        return self.__balance

    def withdraw(self, withdraw):
        if 0 < withdraw <= self.__balance:
            self.__balance -= int(withdraw)
        else:
            print("Invalid withdrawal amount or insufficient balance!")
        return self.__balance

    def get_balance(self):
        return self.__balance

# Account 1
account1 = BankAccount("Utkarsh", "50200032124352", 50000)
account1.deposit(10000)
account1.withdraw(20000)

print(account1.get_balance())