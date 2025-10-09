import tkinter as tk
from tkinter import font, messagebox

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.config(bg="#2c3e50")  # Background color for the window

# Set font styles for widgets
label_font = font.Font(family="Arial", size=14, weight="bold")
button_font = font.Font(family="Arial", size=12)
task_font = font.Font(family="Arial", size=12)

# List to hold tasks
tasks = []

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)  # Clear the entry field
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

# Function to delete a task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks.pop(selected_task_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete!")

# Function to mark a task as done
def mark_done():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = tasks[selected_task_index]
        tasks[selected_task_index] = f"{task} (Done)"
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done!")

# Function to clear all tasks
def clear_all_tasks():
    global tasks
    tasks = []
    update_task_list()

# Function to update the task list display
def update_task_list():
    task_listbox.delete(0, tk.END)  # Clear the listbox before updating
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Entry field for adding a task
task_entry = tk.Entry(root, font=label_font, width=30, bd=3, relief="solid")
task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

# Button to add a task
add_button = tk.Button(root, text="Add Task", font=button_font, bg="#3498db", fg="white", relief="solid", command=add_task)
add_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# Button to delete a task
delete_button = tk.Button(root, text="Delete Task", font=button_font, bg="#e74c3c", fg="white", relief="solid", command=delete_task)
delete_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# Button to mark a task as done
done_button = tk.Button(root, text="Mark Done", font=button_font, bg="#2ecc71", fg="white", relief="solid", command=mark_done)
done_button.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

# Listbox to display the tasks
task_listbox = tk.Listbox(root, font=task_font, width=30, height=10, selectmode=tk.SINGLE, bd=3, relief="solid", bg="#ecf0f1", fg="#34495e")
task_listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Button to clear all tasks
clear_button = tk.Button(root, text="Clear All Tasks", font=button_font, bg="#f39c12", fg="white", relief="solid", command=clear_all_tasks)
clear_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

# Configure grid rows and columns for centering and resizing
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=3)
root.grid_rowconfigure(3, weight=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Start the main event loop
root.mainloop()
