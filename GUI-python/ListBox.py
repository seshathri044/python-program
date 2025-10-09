import tkinter as tk
from tkinter import messagebox

def show_selection():
    selected = listbox.curselection()
    if selected:
        item = listbox.get(selected[0])
        messagebox.showinfo("Selection", f"You selected: {item}")
    else:
        messagebox.showwarning("Warning", "No item selected.")

# Create main window
root = tk.Tk()
root.title("Listbox Example")
root.geometry("300x250")

# Sample items
items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# Create Listbox
listbox = tk.Listbox(root, height=10, selectmode=tk.SINGLE)
for item in items:
    listbox.insert(tk.END, item)
listbox.pack(pady=10)

# Button to show selection
button = tk.Button(root, text="Show Selection", command=show_selection)
button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
