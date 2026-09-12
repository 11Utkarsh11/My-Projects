file = open("Project 11 — Log File Analyzer\log_files.txt", "r")

info = 0
warning = 0
error = 0
len_line = 0
info_line = []
warning_line = []
error_line = []

# Main code
for line in file:
    len_line += 1

    if "INFO" in line:
        info += 1
        info_line.append(line)

    elif "WARNING" in line:
        warning += 1
        warning_line.append(line)
    
    elif "ERROR" in line:
        error += 1
        error_line.append(line)

# Common lines
most_common = 0
if info > warning and info > error:
    most_common = "INFO"

elif warning > error and warning > info:
    most_common = "WARNING"

elif error > warning and error > info:
    most_common = "ERROR"

# Dashboard
while True:
    print("""
====== Log Analyzer ======

What do you want to see?
1. INFO
2. WARNING
3. ERROR
4. All
""")
    
    choice = input("Enter what you choose: ")

    if choice == "1":
        print("\n====== Info ======\n")

        for line in info_line:
            print(line.strip())

    elif choice == "2":
        print("\n====== Warnings ======\n")

        for line in warning_line:
            print(line.strip())

    elif choice == "3":
        print("====== Errors ======\n")

        for line in error_line:
            print(line.strip())

    elif choice == "4":
        print(f"""
====== Log Analyzer ======

Total lines: {len_line}

INFO:     {info}
WARNING:  {warning}
ERROR:    {error}

Most common level: {most_common}
""")

    else:
        print("Invalid option! Enter between (1-4)")


file.close() 