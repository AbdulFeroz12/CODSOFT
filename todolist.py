import os
import json

class ToDoList:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "Done" if task["completed"] else "Pending"
                print(f"{idx}. {task['task']} [{status}]")

    def mark_task_as_done(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            self.save_tasks()
            print(f"Task '{self.tasks[task_number - 1]['task']}' marked as done.")
        else:
            print("Invalid task number.")

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"Task '{removed_task['task']}' removed.")
        else:
            print("Invalid task number.")

    def clear_tasks(self):
        self.tasks = []
        self.save_tasks()
        print("All tasks cleared.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Mark Task as Done")
        print("5. Clear All Tasks")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
            
        elif choice == '2':
            try:
                task_number = int(input("Enter the task number to remove: "))
                todo_list.remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            try:
                task_number = int(input("Enter the task number to mark as done: "))
                todo_list.mark_task_as_done(task_number)
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '5':
            todo_list.clear_tasks()
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
