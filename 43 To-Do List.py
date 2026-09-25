import os

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
    print(f"\nTask '{task}' added!")


def view_tasks():
    if len(tasks) == 0:
        print("\n📋 MY TO-DO LIST")
        print("No tasks yet!")
        return

    print("\n📋 MY TO-DO LIST")
    print("========================")

    for i, task in enumerate(tasks):
        if task["done"]:
            print(f"{i + 1}. {task['task']} ✅")
        else:
            print(f"{i + 1}. {task['task']}")

    print("========================")


def mark_done():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        number = int(input("\nEnter task number to mark done: "))
        tasks[number - 1]["done"] = True
        print(f"\n🎉 Task '{tasks[number - 1]['task']}' marked as done!")

    except IndexError:
        print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


def delete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        number = int(input("\nEnter task number to delete: "))
        removed = tasks.pop(number - 1)
        print(f"\n🗑️ Task '{removed['task']}' deleted!")

    except IndexError:
        print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            status = "done" if task["done"] else "pending"
            file.write(f"{task['task']},{status}\n")

    print("\n💾 Tasks saved successfully!")


def load_tasks():
    tasks.clear()
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                line = line.strip()

                if line:
                    parts = line.split(",")
                    task = parts[0]
                    done = True if parts[1] == "done" else False
                    tasks.append({"task": task, "done": done})

        if len(tasks) > 0:
            print("📂 Tasks loaded successfully!")
        else:
            print("No saved tasks found!")

    except FileNotFoundError:
        print("No saved tasks found!")


def main():

    print("================================")
    print("      📋 TO-DO LIST APP")
    print("================================")

    load_tasks()

    input("\nPress Enter to continue...")

    while True:

        show_menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_task()

            elif choice == 2:
                view_tasks()

            elif choice == 3:
                mark_done()

            elif choice == 4:
                delete_task()

            elif choice == 5:
                save_tasks()

            elif choice == 6:
                load_tasks()

            elif choice == 7:
                save_tasks()
                print("\n✨ Goodbye! Keep being productive! 😄")
                break

            else:
                print("\n⚠️ Invalid choice! Enter 1 to 7!")

        except ValueError:
            print("\n⚠️ Please enter a valid number!")

        if choice != 7:
            input("\nPress Enter to continue...")


main()