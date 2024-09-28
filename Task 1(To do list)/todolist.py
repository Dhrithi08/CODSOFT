import tkinter as tk
from tkinter import messagebox
import json
import os

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        self.root.config(bg="#e0f7fa")

        self.tasks = []  # List to hold tasks
        self.task_var = tk.StringVar()  # Variable for task entry
        self.priority_var = tk.StringVar(value="Low")  # Variable for priority

        # Task Listbox (initialize first)
        self.task_listbox = tk.Listbox(self.root, width=50, height=15, font=("Arial", 12), bg="#ffffff")
        self.task_listbox.pack(pady=10)

        # Heading
        self.heading = tk.Label(self.root, text="TO DO LIST", font=("Arial", 20, "bold"), bg="#e0f7fa", fg="#333")
        self.heading.pack(pady=10)

        # Frame for task entry and buttons
        self.frame = tk.Frame(self.root, bg="#e0f7fa")
        self.frame.pack(pady=10)

        # Task Entry
        self.task_entry = tk.Entry(self.frame, textvariable=self.task_var, width=30, font=("Arial", 12))
        self.task_entry.pack(pady=10)

        # Priority Frame
        self.priority_frame = tk.Frame(self.root, bg="#e0f7fa")
        self.priority_frame.pack(pady=10)

        # Radio Buttons for Priority
        self.create_priority_radio_buttons()

        # Load tasks from a file
        self.load_tasks()

        # Buttons for Add, Update, Remove, and Toggle Task
        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task, font=("Arial", 12), bg="#4caf50", fg="white")
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(self.frame, text="Update Task", command=self.update_task, font=("Arial", 12), bg="#ff9800", fg="white")
        self.update_button.pack(pady=5)

        self.remove_button = tk.Button(self.frame, text="Remove Task", command=self.remove_task, font=("Arial", 12), bg="#f44336", fg="white")
        self.remove_button.pack(pady=5)

        self.toggle_button = tk.Button(self.frame, text="Toggle Completion", command=self.toggle_task_completion, font=("Arial", 12), bg="#2196f3", fg="white")
        self.toggle_button.pack(pady=5)

    def create_priority_radio_buttons(self):
        """Create radio buttons for task priority."""
        low_priority = tk.Radiobutton(self.priority_frame, text="Low", variable=self.priority_var, value="Low", font=("Arial", 12), bg="#4caf50", fg="white")
        low_priority.grid(row=0, column=0, padx=5, pady=5)

        medium_priority = tk.Radiobutton(self.priority_frame, text="Medium", variable=self.priority_var, value="Medium", font=("Arial", 12), bg="#ff9800", fg="white")
        medium_priority.grid(row=0, column=1, padx=5, pady=5)

        high_priority = tk.Radiobutton(self.priority_frame, text="High", variable=self.priority_var, value="High", font=("Arial", 12), bg="#f44336", fg="white")
        high_priority.grid(row=0, column=2, padx=5, pady=5)

    def add_task(self):
        """Add a new task to the list."""
        task = self.task_var.get().strip()
        if task:
            priority = self.priority_var.get()
            self.tasks.append({"task": task, "completed": False, "priority": priority})
            self.update_task_list()
            self.save_tasks()  # Save after adding a task
            self.task_var.set("")  # Clear the task entry
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")
        self.task_entry.focus()

    def update_task(self):
        """Update the description of the selected task."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            new_task = self.task_var.get().strip()
            if new_task:
                self.tasks[selected_index]["task"] = new_task
                self.tasks[selected_index]["priority"] = self.priority_var.get()
                self.update_task_list()
                self.save_tasks()  # Save after updating a task
                self.task_var.set("")  # Clear the task entry
            else:
                messagebox.showwarning("Input Error", "Please enter the updated task description.")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to update.")
        self.task_entry.focus()

    def remove_task(self):
        """Remove the selected task from the list."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_list()
            self.save_tasks()  # Save after removing a task
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")
        self.task_entry.focus()

    def toggle_task_completion(self):
        """Toggle the completion status of the selected task."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]["completed"] = not self.tasks[selected_index]["completed"]
            self.update_task_list()
            self.save_tasks()  # Save after toggling completion
            messagebox.showinfo("Toggle Status", f"Task '{self.tasks[selected_index]['task']}' marked as {'completed' if self.tasks[selected_index]['completed'] else 'incomplete'}.")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to toggle completion.")
        self.task_entry.focus()

    def update_task_list(self):
        """Refresh the task listbox."""
        self.task_listbox.delete(0, tk.END)  # Clear the listbox
        for task in self.tasks:
            completed_marker = '[X]' if task['completed'] else '[ ]'
            self.task_listbox.insert(tk.END, f"{completed_marker} {task['task']} ({task['priority']})")

    def save_tasks(self):
        """Save tasks to a JSON file."""
        with open('tasks.json', 'w') as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        """Load tasks from a JSON file."""
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r') as f:
                self.tasks = json.load(f)
                self.update_task_list()

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()
