import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

# Load existing tasks and ensure they have the 'completed' key
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            try:
                tasks = json.load(file)
                # Ensure all tasks have 'completed' key
                for task in tasks:
                    if "completed" not in task:
                        task["completed"] = False
                return tasks
            except json.JSONDecodeError:
                return []  # If file is corrupt, return an empty list
    return []

# Save tasks to file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task():
    task_text = entry_task.get().strip()
    if task_text:
        tasks.append({"task": task_text, "completed": False})
        update_listbox()
        save_tasks()
        entry_task.delete(0, tk.END)

# Mark selected task as completed
def complete_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        tasks[selected_index]["completed"] = True
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task!")

# Delete selected task
def delete_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        del tasks[selected_index]
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task!")

# Update the task list display
def update_listbox():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task.get("completed", False) else "❌"  # Fix applied here
        listbox_tasks.insert(tk.END, f"{status} {task['task']}")

# Create GUI window
root = tk.Tk()
root.title("To-Do List")

# Load tasks
tasks = load_tasks()

# Input field and buttons
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=5)
btn_add = tk.Button(root, text="Add Task", command=add_task)
btn_add.pack()

# Task list display
listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.pack(pady=5)
update_listbox()

# Action buttons
btn_complete = tk.Button(root, text="Mark Completed", command=complete_task)
btn_complete.pack(pady=5)
btn_delete = tk.Button(root, text="Delete Task", command=delete_task)
btn_delete.pack()

# Run the GUI loop
root.mainloop()
