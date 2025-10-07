import tkinter as tk
root = tk.Tk()
root.title("Calculator")
root.geometry("400x300")
label = tk.Label(root, text="Enter two numbers to Calculate")
label.pack()
a = tk.Entry(root)
a.pack()
b = tk.Entry(root)
b.pack()
def add():
    result = float(a.get()) + float(b.get())
    label.config(text="Result: " + str(result))
button = tk.Button(root, text="Addition", command=add)
def sub():
    result = float(a.get()) - float(b.get())
    label.config(text="Result: " + str(result))
button = tk.Button(root, text="Subtract", command=sub)
button.pack()
def mul():
    result = float(a.get()) * float(b.get())
    label.config(text="Result: " + str(result))
button = tk.Button(root, text="Multiplication", command=mul)
button.pack()
def div():
    result = float(a.get()) / float(b.get())
    label.config(text="Result: " + str(result))
button = tk.Button(root, text="Division", command=div)
button.pack()
def quit():
    root.destroy()
button = tk.Button(root, text="Quit", command=quit)
button.pack()
root.mainloop()