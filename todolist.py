import json
import os
from datetime import datetime

class ToDoList:
    def __init__(self, filename="todo_list.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        else:
            return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=2)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task['title']} - {task['date']}")

    def add_task(self, title):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_task = {"title": title, "date": date}
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task added: {title}")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            deleted_task = self.tasks.pop(index - 1)
            self.save_tasks()
            print(f"Task deleted: {deleted_task['title']}")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n===== To-Do List =====")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            todo_list.display_tasks()
        elif choice == "2":
            title = input("Enter task title: ")
            todo_list.add_task(title)
        elif choice == "3":
            index = int(input("Enter task index to delete: "))
            todo_list.delete_task(index)
        elif choice == "4":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
