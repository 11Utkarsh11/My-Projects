To_Do = """
====== To-Do List ======

1. Add task
2. View tasks
3. Remove task
4. Exit

"""
print(To_Do)
task = []

while True:

    option = input("Chose an option: ")

    if option == "1":

        print("To quit entering tasks, press e")

        while True:
            entered_task = input("Enter task: ")

            if entered_task.lower() == "e":
                break
            task.append(entered_task)

        print(To_Do)

    elif option == "2":
        print("====== Your Tasks ======")

        for number,values in enumerate(task, start=1):
            print(f"{number}. {values}")

        print(To_Do)
        
    elif option == "3":
        print("====== Removable Tasks ======")

        for number, values in enumerate(task, start=1):
            print(f"{number}. {values}")

        remove_task = int(input("Enter the task number you want to remove: "))

        if 1 <= remove_task <= len(task):
            removed_task = task.pop(remove_task - 1)
            print(f"Task removed: {removed_task}")

            print("====== Remaining Tasks After Removal ======")
        
            for number, values in enumerate(task, start=1):
                print(f"{number}. {values}")

        else:
            print("Invalid task number.")

        print(To_Do)

    elif option == "4":
        break