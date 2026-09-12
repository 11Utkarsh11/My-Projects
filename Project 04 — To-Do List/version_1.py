
print("====== To-Do List ======\n")
print("1. Add task")
print("2. View tasks")
print("3. Remove task")
print("4. Exit\n")

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

    elif option == "2":
        print(task)

    elif option == "3":
        remove_task = input("Enter the task you want to remove: ")
        if remove_task in task:
            task.remove(remove_task)
            print("Task removed.")
        else:
            print("Task not found.")
        print(task)
        
    elif option == "4":
        break