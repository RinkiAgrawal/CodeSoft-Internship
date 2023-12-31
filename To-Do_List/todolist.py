import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, f"{len(tasks_listbox.get(0, tk.END))+1}. {task}")
        task_entry.delete(0, tk.END)
        status_label.config(text="Task successfully added.", fg="green")
    else:
        status_label.config(text="Please enter a task.", fg="red")

def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
        # Re-number tasks after deletion
        for i, task in enumerate(tasks_listbox.get(0, tk.END), start=1):
            tasks_listbox.delete(i-1)
            tasks_listbox.insert(tk.END, f"{i}. {task.split('. ', 1)[1]}")
        status_label.config(text="Task deleted.", fg="green")
    else:
        status_label.config(text="Please select a task to delete.", fg="red")

def clear_all_tasks():
    tasks_listbox.delete(0, tk.END)
    status_label.config(text="All tasks cleared.", fg="green")

# Create the main application window
app = tk.Tk()
app.title("To-Do List App")
app.configure(bg='lightgray')  # Set background color

# Add a greeting label
greeting_label = tk.Label(app, text="Welcome! Enter your task below:", bg='lightgray')
greeting_label.pack(pady=5)

# Create and configure widgets
tasks_listbox = tk.Listbox(app, width=50)
tasks_listbox.pack(pady=10)

task_entry = tk.Entry(app, width=50)
task_entry.pack(pady=5)

add_button = tk.Button(app, text="Add Task", width=24, command=add_task, bg='green', fg='white')
add_button.pack(side=tk.LEFT, padx=5, pady=5)

delete_button = tk.Button(app, text="Delete Task", width=24, command=delete_task, bg='red', fg='white')
delete_button.pack(side=tk.RIGHT, padx=5, pady=5)

clear_all_button = tk.Button(app, text="Clear All", width=24, command=clear_all_tasks, bg='orange', fg='white')
clear_all_button.pack(side=tk.LEFT, padx=5, pady=5)

# Add a status label for feedback messages
status_label = tk.Label(app, text="", fg="green", bg='lightgray')
status_label.pack(pady=5)

app.mainloop()