import tkinter as tk

def disp():
    ak = tk.Label(root, text="Python Application")
    ak.pack()

root = tk.Tk()
root.title("Instagram Program") 
root.iconbitmap('instagram_logo_icon_267526.ico')

# Welcome label
label = tk.Label(root, text="Welcome")
label.pack()

# Button with a function call
ac = tk.Button(root, text="New", command=disp)
ac.pack()

# A label with 'hi'
a = tk.Label(root, text="hi")
a.pack()

root.mainloop()
