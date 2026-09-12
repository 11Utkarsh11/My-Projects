contacts = []


def main_menu():
    while True:

        print("""
================================
         CONTACT BOOK
================================

1. Add Contact
2. View Contacts
3. Search Contact
4. Delete Contact
5. Exit
""")

        choice = input("Enter a choice here: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            delete_contact()

        elif choice == "5":
            break

        else:
            print("Invalid choice!")
            continue


def add_contact():
    print("""
================================
          ADD CONTACT
================================
""")

    name = input("Name: ")
    phone_num = input("Phone number: ")
    email = input("Email: ")

    contacts.append({"name": name,
                    "phone": phone_num,
                    "email": email
                    })

    print(f"\nContact named {name} added to your phonebook")


def view_contacts():
    if contacts:
        print("""
================================
        YOUR CONTACTS
================================
""")

        for number,contact in enumerate(contacts, start=1):
            print(f"{number}. {contact["name"]}\nPhone: {contact["phone"]}\nEmail: {contact["email"]}\n")

    else:
        print("Contact list is empty.")


def search_contact():
    option = input("Enter contact name to search: ")
    found = False

    for contact in contacts:
        if option == contact["name"]:
            print("""
================================
        CONTACT FOUND
================================
""")
            print(f"Name: {contact["name"]}\nPhone: {contact["phone"]}\nEmail: {contact["email"]}")
            found = True
            break

    if not found:
        print("Contact not found!")

def delete_contact():
    if not contacts:
        print("Contact list is empty.")
        return
    
    option = input("Enter contact name to delete: ")
    found = False

    for contact in contacts:
        if option == contact["name"]:
            print("""
================================
        CONTACT FOUND
================================
""")
            print(f"Name: {contact["name"]}\nPhone: {contact["phone"]}\nEmail: {contact["email"]}")
            found = True

            option2 = input("Are you sure you want to delete this contact? (y/n): ")

            if option2 == "y":
                contacts.remove(contact)
                print("Contact deleted successfully")
                break

            elif option2 == "n":
                break

    if not found:
        print("Contact not found!")
        

main_menu()