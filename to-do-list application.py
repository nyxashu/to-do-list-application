import json
import os

FILE_PATH = 'todos.json'

def load_tasks():
    """Load tasks from a file."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to a file."""
    with open(FILE_PATH, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def view_tasks():
    """View all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def delete_task(task_number):
    """Delete a task by its number."""
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task}' deleted.")
    else:
        print("Invalid task number.")

def main():
    """Main function to run the application."""
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_number)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
