import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter Program")  # Set window title

# Function to display a message when button is clicked
def display_message():
    label.config(text="Hello, Tkinter!")
    print("bye")
# Create a Label widget
label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 14))
label.pack(pady=20)

# Create a Button widget
button = tk.Button(root, text="Click Me!", command=display_message, font=("Arial", 12))
button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
