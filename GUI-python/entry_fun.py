import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Entry Widget Example")

# Function to get text from Entry and display it in the Label
def show_entry_text():
    entered_text = entry.get()  # Get text from Entry widget
    label.config(text=f"You typed: {entered_text}")

# Entry widget for user input
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Button to trigger the display function
button = tk.Button(root, text="Show Text", command=show_entry_text, font=("Arial", 12))
button.pack(pady=5)

# Label to show the entered text
label = tk.Label(root, text="", font=("Arial", 14))
label.pack(pady=10)

# Run the app
root.mainloop()