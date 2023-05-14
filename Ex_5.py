tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added.")

def remove_task():
    task = input("Enter task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print("Task removed.")
    else:
        print("Task not found.")

def show_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

while True:
    print("Select an option:")
    print("1. Add task")
    print("2. Remove task")
    print("3. Show tasks")
    print("4. Exit")
    choice = input("> ")

    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        show_tasks()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
