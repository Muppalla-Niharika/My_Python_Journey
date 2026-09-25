tasks = []
def show_menu():
    print("\n===== To-Do List App =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Done")
    print("4. Delete Task")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("7. Exit")
    print("==========================")
def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added!")
def view_tasks():
    if len(tasks) == 0:
        print("No tasks yet!")
        return
    print("\n===== Your Tasks =====")
    for i, task in enumerate(tasks):
        status = "✅" if task["done"] else "❌"
        print(f"{i+1}. {status} {task['task']}")
    print("======================")
def mark_done():
    view_tasks()
    try:
        number = int(input("Enter task number to mark done: "))
        tasks[number-1]["done"] = True
        print(f"Task {number} marked as done!")
    except IndexError:
        print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")
def delete_task():
    view_tasks()
    try:
        number = int(input("Enter task number to delete: "))
        removed = tasks.pop(number-1)
        print(f"Task '{removed['task']}' deleted!")
    except IndexError:
        print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")