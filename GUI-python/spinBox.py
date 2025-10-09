import tkinter as tk
def on_spinbox_changes():
    value = spinbox.get()
    print(f"SPinbox value:{value}")
root = tk.Tk()
root.title("Spinbox")
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(2,weight=1)
root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(2,weight=1)

label=tk.Label(root,text="seshathri",fg="black")
label.grid(row=0,column=1)
def Show_val():
    value= spinbox.get()
    root.config(bg=f"#{int(value)*25:02x}{int(value)*25:02x}{int(value)*25:02x}")
    label.config(font=("Helvetica",int(value)*10))
a=[2,3,4,6,8]
spinbox = tk.Spinbox(root,from_=0,to=10,wrap=True,width=5,fg="blue",font=("Helventica",24),justify="center",command=Show_val)
spinbox.grid(row=2,column=1)
spinbox1 = tk.Spinbox(root,values=a,wrap=True,width=5,fg="blue",font=("Helventica",24),justify="center",command=Show_val)
spinbox1.grid(row=1,column=1)


# Sample items
items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
# Create Listbox
listbox = tk.Listbox(root, height=10, selectmode=tk.SINGLE)
for item in items:
    listbox.insert(tk.END, item)
listbox.grid(row=3,column=1)
# Button to show selection
button = tk.Button(root, text="Show Selection")
button.grid(row=4,column=1,pady=5)

root.mainloop()