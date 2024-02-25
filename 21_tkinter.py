import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        self.task_listbox = tk.Listbox(master, width=50, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.complete_button = tk.Button(master, text="Mark as Complete", command=self.mark_as_complete)
        self.complete_button.grid(row=2, column=0, padx=5, pady=5)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=5, pady=5)

        self.refresh_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.refresh_tasks()
            self.task_entry.delete(0, tk.END)

    def mark_as_complete(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index] = f"{self.tasks[index]} (Completed)"
            self.refresh_tasks()
        except IndexError:
            messagebox.showinfo("Error", "Please select a task to mark as complete.")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.refresh_tasks()
        except IndexError:
            messagebox.showinfo("Error", "Please select a task to delete.")

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
