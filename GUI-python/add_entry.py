import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Function to get text from Entry, add numbers, and display the result
def add():
    try:
        num1 = float(a.get())  # Convert input to float
        num2 = float(b.get())  # Convert input to float
        result = num1 + num2
        label.config(text=f"Result = {result}")
    except ValueError:
        label.config(text="Please enter valid numbers")

# Entry widget for the first number
a = tk.Entry(root, font=("Arial", 14))
a.pack(pady=10)

# Entry widget for the second number
b = tk.Entry(root, font=("Arial", 14))
b.pack(pady=10)

# Button to trigger the add function
button = tk.Button(root, text="Add", command=add, font=("Arial", 12))
button.pack(pady=10)

# Label to show the result
label = tk.Label(root, text="", font=("Arial", 14))
label.pack(pady=20)

# Run the app
root.mainloop()
