tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"'{task}' added to the list.")

def update_task():
    if not tasks:
        print("\nNo tasks available.")
        return
    show_tasks()
    try:
        task_num = int(input("\nEnter the task number to update: ")) - 1
        if 0 <= task_num < len(tasks):
            new_task = input("Enter the new task: ")
            tasks[task_num] = new_task
            print(f"Task {task_num + 1} updated to '{new_task}'.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task():
    if not tasks:
        print("\nNo tasks available.")
        return
    show_tasks()
    try:
        task_num = int(input("\nEnter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print(f"'{removed_task}' removed from the list.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")


while True :
    print("\nOptions:")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting the application. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")

