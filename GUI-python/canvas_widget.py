import tkinter as tk 
from tkinter import Canvas
from tkinter import ttk
root = tk.Tk()
root.title("Canvas Example")
root.geometry("400x300")
root.config(bg="#2e2e2e")
canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=20)
def draw_rectangle():
    canvas.create_rectangle(100, 50, 200, 150, fill="blue")
def draw_circle():
    canvas.create_oval(50, 50, 150, 150, fill="red")
def draw_line():
    canvas.create_line(0, 0, 300, 200, fill="green", width=2)
def draw_text():
    canvas.create_text(150, 100, text="Hello, Canvas!", fill="black", font=("Arial", 10))
combo = ttk.Combobox(root, values=["Draw Rectangle", "Draw Circle", "Draw Line", "Draw Text"])
combo.current(0)
combo.pack(pady=10)
def on_select(event):
    selection = combo.get()
    canvas.delete("all")
    if selection == "Draw Rectangle":
        draw_rectangle()
    elif selection == "Draw Circle":
        draw_circle()
    elif selection == "Draw Line":
        draw_line()
    elif selection == "Draw Text":
        draw_text()
combo.bind("<<ComboboxSelected>>", on_select) 
root.mainloop()