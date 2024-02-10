import os

def display_menu():
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

def load_tasks():
    tasks = []
    file_path = "todo_list.txt"

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            tasks = [line.strip() for line in file.readlines()]

    return tasks

def save_tasks(tasks):
    file_path = "todo_list.txt"

    with open(file_path, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_todo_list(tasks):
    if not tasks:
        print("No tasks in the To-Do List.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully.")

def mark_completed(tasks):
    view_todo_list(tasks)
    try:
        index = int(input("Enter the index of the task to mark as completed: ")) - 1
        tasks[index] = "[Completed] " + tasks[index]
        print("Task marked as completed.")
    except IndexError:
        print("Invalid index.")

def remove_task(tasks):
    view_todo_list(tasks)
    try:
        index = int(input("Enter the index of the task to remove: ")) - 1
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task}' removed.")
    except IndexError:
        print("Invalid index.")

def main():
    tasks = load_tasks()

    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_todo_list(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Exiting. Your To-Do List has been saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
