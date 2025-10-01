# To-Do List

tasks = []

while True:
    print("\nYour Tasks:", tasks)
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Task removed!")
        else:
            print("Task not found.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
