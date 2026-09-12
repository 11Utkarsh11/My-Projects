To_Do = """
====== To-Do List ======

1. Add task
2. View tasks
3. Remove task
4. Exit
"""
print(To_Do)
task = []
emojis = []

while True:
    option = input("Chose an option: ")

    if option == "1":

        print("\nTo quit entering tasks, press e")

        while True:
            entered_task = input("Enter task: ")

            if entered_task.lower() == "e":
                break
            task.append(entered_task)
            emojis.append("⬜")

        print(To_Do)

    elif option == "2":
        print("\n====== Your Tasks ======")

        for number,values in enumerate(task, start=1):
            print(f"{number}. {values} {emojis[number - 1]}")

        completed_task = int(input("Enter task number to mark as completed: "))

        if 1 <= completed_task <= len(task):
            emojis[completed_task - 1] = "✅"

        else:
            print("Enter valid number")

        print("\n====== Updated Tasks ======")
        
        for number,values in enumerate(task, start=1):
            print(f"{number}. {values} {emojis[number - 1]}")

        print(To_Do)
        
    elif option == "3":
        print("\n====== Removable Tasks ======")

        for number, values in enumerate(task, start=1):
            print(f"{number}. {values} {emojis[number - 1]}")

        remove_task = int(input("Enter the task number you want to remove: "))

        if 1 <= remove_task <= len(task):
            removed_task = task.pop(remove_task - 1)
            emojis.pop(remove_task - 1)
            print(f"Task removed: {removed_task}")

            print("\n====== Remaining Tasks After Removal ======")
        
            for number, values in enumerate(task, start=1):
                print(f"{number}. {values} {emojis[number - 1]}")

        else:
            print("Invalid task number.")

        print(To_Do)

    elif option == "4":
        break