todo_list = []
def show_tasks():
    if not todo_list:
        print("No tasks yet.")
    else:
        for i, task in enumerate(todo_list,1):
            print(f"{i}.{task}")
def add_task(task):
    todo_list.append(task)
    print("task added")
def delete_task(index):
    if 0 < index <= len(todo_list):
        removed =todo_list.pop(index - 1)
        print(f"Deleted : {removed}")
    else:
        print("Invalid task number .")
while True:
    print("\n=== To-Do List ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")
    if choice == '1':
        show_tasks()
    elif choice == '2':
        task = input("Enter task")
        add_task(task)
    elif choice == '3':
        if not todo_list:
            print("No tasks to delete.")
        else:
            show_tasks()
        try:
            idx = int(input("Enter task number to delete"))
            delete_task(idx)
        except ValueError:
            print("Please enter a valid number .")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid option")

