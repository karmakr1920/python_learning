import json

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        json.dump(tasks, f)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, (name, done) in enumerate(tasks, 1):
            status = "✔" if done else "✘"
            print(f"{i}. [{status}] {name}")

def add_task(tasks):
    name = input("Enter new task: ").strip()
    if name:
        tasks.append([name, False])
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Task cannot be empty.")

def mark_task_done(tasks):
    if not tasks:
        print("No tasks to mark as done.")
        return
    display_tasks(tasks)
    try:
        idx = int(input("Enter task number to mark as done: "))
        if 1 <= idx <= len(tasks):
            tasks[idx - 1][1] = True
            save_tasks(tasks)
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return
    display_tasks(tasks)
    try:
        idx = int(input("Enter task number to delete: "))
        if 1 <= idx <= len(tasks):
            removed = tasks.pop(idx - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed[0]}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def edit_task(tasks):
    if not tasks:
        print("No tasks to edit.")
        return
    display_tasks(tasks)
    try:
        idx = int(input("Enter task number to edit: "))
        if 1 <= idx <= len(tasks):
            new_name = input("Enter new task description: ").strip()
            if new_name:
                tasks[idx - 1][0] = new_name
                save_tasks(tasks)
                print("Task updated.")
            else:
                print("Task cannot be empty.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def view_completed(tasks):
    completed = [task for task in tasks if task[1]]
    if not completed:
        print("No completed tasks.")
    else:
        for i, task in enumerate(completed, 1):
            print(f"{i}. ✔ {task[0]}")

def view_uncompleted(tasks):
    uncompleted = [task for task in tasks if not task[1]]
    if not uncompleted:
        print("No uncompleted tasks.")
    else:
        for i, task in enumerate(uncompleted, 1):
            print(f"{i}. ✘ {task[0]}")

def show_menu():
    print("\n--- To-Do List ---")
    print("1. View all tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Edit task")
    print("6. View completed tasks")
    print("7. View uncompleted tasks")
    print("8. Exit")

def todo_app():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-8): ")

        match choice:
            case "1": display_tasks(tasks)
            case "2": add_task(tasks)
            case "3": mark_task_done(tasks)
            case "4": delete_task(tasks)
            case "5": edit_task(tasks)
            case "6": view_completed(tasks)
            case "7": view_uncompleted(tasks)
            case "8":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please choose between 1–8.")

todo_app()
