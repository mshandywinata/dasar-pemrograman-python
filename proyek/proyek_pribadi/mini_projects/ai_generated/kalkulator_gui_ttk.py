import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

def calculate(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = ThemedTk(theme="arc")  # Use a theme for a better look
root.title("Calculator")

screen = tk.StringVar()

entry = ttk.Entry(root, textvar=screen)
entry.grid(row=0, column=0, columnspan=4, sticky='ew')

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['.', '0', '=', '+']
]

for i in range(4):
    for j in range(4):
        button = ttk.Button(root, text=buttons[i][j])
        button.grid(row=i + 1, column=j, sticky='nsew')
        button.bind("<Button-1>", calculate)

clear = ttk.Button(root, text="C")
clear.grid(row=5, column=0, sticky='nsew')
clear.bind("<Button-1>", calculate)

# Make the buttons resize with the window
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
