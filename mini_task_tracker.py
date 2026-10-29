
import json
import os

FILE_NAME = "tasks.json"


# Load tasks from JSON file
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            tasks = json.load(file)

        if not isinstance(tasks, list):
            print("Invalid file format. Starting with an empty task list.")
            return []

        return tasks

    except (json.JSONDecodeError, OSError):
        print("Could not load tasks.json. Starting with an empty task list.")
        return []


# Save tasks to JSON file
def save_tasks():
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)
    except OSError:
        print("Error: Tasks could not be saved.")


# Add a new task
def add_task():
    title = input("Task title: ").strip()

    if not title:
        print("Error: Task title cannot be empty.")
        return

    tasks.append({"title": title, "done": False})
    save_tasks()
    print("Task added.")


# View all tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{number}. {task['title']} [{status}]")


# Complete a task
def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Task number: "))

        if number < 1 or number > len(tasks):
            print("Error: Invalid task number.")
            return

        tasks[number - 1]["done"] = True
        save_tasks()
        print("Task completed.")

    except ValueError:
        print("Error: Please enter a valid number.")


# Delete a task
def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Task number: "))

        if number < 1 or number > len(tasks):
            print("Error: Invalid task number.")
            return

        removed_task = tasks.pop(number - 1)
        save_tasks()
        print(f"Task '{removed_task['title']}' deleted.")

    except ValueError:
        print("Error: Please enter a valid number.")


# Load saved tasks when the program starts
tasks = load_tasks()


# Main menu
while True:
    print("\n--- TASK TRACKER ---")
    print("1. Add")
    print("2. View")
    print("3. Complete")
    print("4. Delete")
    print("5. Exit")

    choice = input("Choice: ").strip()

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Tasks saved. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1-5.")