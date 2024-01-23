import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []
        self.create_widgets()

    def create_widgets(self):
        self.task_entry = tk.Entry(self.root, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, height=10, width=40)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        delete_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def add_task(self):
        task_title = self.task_entry.get().strip()
        if task_title:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            task_info = f"{task_title} - {date}"
            self.tasks.append(task_info)
            self.task_listbox.insert(tk.END, task_info)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task title cannot be empty.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index[0]]
        else:
            messagebox.showwarning("Warning", "Select a task to delete.")

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
