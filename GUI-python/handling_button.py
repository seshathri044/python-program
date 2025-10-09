import tkinter as tk
def on_button_click(event):
    ak=tk.Label(root,text="Button Clicked!").pack()
root=tk.Tk()
button=tk.Button(root,text="Click Me")
button.pack()
button.bind("<Button-1>",on_button_click)


root.mainloop()