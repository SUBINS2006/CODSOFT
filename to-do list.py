# Task 1 - To-Do List Application
todo_list = []

def show_menu():
    print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Done\n4. Exit")

def add_task():
    task = input("Enter a task: ")
    todo_list.append({"task": task, "done": False})
    print("Task added.")

def view_tasks():
    if not todo_list:
        print("No tasks yet!")
    else:
        for i, task in enumerate(todo_list, 1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i}. {task['task']} [{status}]")

def mark_done():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(todo_list):
            todo_list[num-1]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
