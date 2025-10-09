import tkinter as tk
from PIL import Image, ImageTk  # Import PIL for image processing

# Create the main window
root = tk.Tk()
root.title("Monkey D Luffy")
root.geometry("600x600")  # Set window size

# Set background color
root.configure(bg='lightblue')  # You can change this to any color you like

# Load the image using Pillow
img = Image.open("luffy.jpg")  # Change to your image path
#img = img.resize((600,600))  # Optional: Resize the image if needed

# Convert the image to a format Tkinter can use
img_tk = ImageTk.PhotoImage(img)

# Display the image in the window
img_label = tk.Label(root, image=img_tk)
img_label.pack(pady=50)  # Adjust the padding as needed

# Keep a reference to the image object (important for Tkinter)
img_label.image = img_tk

# Run the main event loop
root.mainloop()
