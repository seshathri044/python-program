import tkinter as tk
def on():
    a=int(text1.get())
    b=int(text2.get())
    print(a+b)
root=tk.Tk()
text1=tk.Entry(root)
text2=tk.Entry(root)
button=tk.Button(root,text="Add",command=on)
text1.grid(row=0,column=0)
text2.grid(row=0,column=1)
button.grid()
root.mainloop()