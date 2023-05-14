contacts = {}

while True:
    print("\n---- Contact List ----")
    print("1. Add contact")
    print("2. Remove contact")
    print("3. Show contacts")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter the name: ")
        number = input("Enter the phone number: ")
        contacts[name] = number
        print(f"{name} added to contacts")
    elif choice == "2":
        name = input("Enter the name to remove: ")
        if name in contacts:
            del contacts[name]
            print(f"{name} removed from contacts")
        else:
            print(f"{name} not found in contacts")
    elif choice == "3":
        print("\n---- Contacts ----")
        for name, number in contacts.items():
            print(f"{name}: {number}")
    elif choice == "4":
        print("Exiting contact list...")
        break
    else:
        print("Invalid choice. Try again.")
