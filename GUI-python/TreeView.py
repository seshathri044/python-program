import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.config(bg="black")
root.title("Student Information")
root.geometry("500x300")

# Create the Treeview widget with multiple columns
treeview = ttk.Treeview(root, columns=("RollNo", "Name", "Age"),height=4)

# Define the columns
treeview.heading("#0", text="ID")
treeview.heading("RollNo", text="Roll No")
treeview.heading("Name", text="Name")
treeview.heading("Age", text="Age")

# Configure the column width
treeview.column("#0", width=100, anchor="center")
treeview.column("RollNo", width=100, anchor="center")
treeview.column("Name", width=100, anchor="center")
treeview.column("Age", width=100, anchor="center")

# Insert rows of data (student information)
treeview.insert("", "end", text="1", values=("101", "John Doe", "20"))
treeview.insert("", "end", text="2", values=("102", "Jane Smith", "22"))
treeview.insert("", "end", text="3", values=("103", "Mark Brown", "21"))
treeview.insert("", "end", text="4", values=("104", "Lucy Green", "23"))

# Pack the treeview widget
treeview.pack(pady=250)

# Run the Tkinter event loop
root.mainloop()
