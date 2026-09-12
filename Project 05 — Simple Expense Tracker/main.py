exp_tracker = """
====== Expense Tracker ======

1. Add expense
2. View expenses
3. Show total
4. Exit
"""
print(exp_tracker)

expenses = []

while True:
    entered_value = input("Choose an option: ")

    # Add expense
    if entered_value == "1":

        expense = input("\nEnter Your expense here: ")
        amount = int(input("Enter expense amount: "))
        expenses.append({expense : amount})

        print(exp_tracker)

    # View expense
    elif entered_value == "2":
        print("\n====== Your Expenses ======\n")

        for number, expense in enumerate(expenses, start=1):
            for name, amount in expense.items():
                print(f"{number}. {name} - ₹{amount}")

        print(exp_tracker)

    # Total expense
    elif entered_value == "3":
        total = 0

        print("\n====== Total ======")

        for expense in expenses:
            for amount in expense.values():
                total += amount
        print(f"\nTotal expenses: ₹{total}")

        print(exp_tracker)

    # Exit
    elif entered_value == "4":
        break