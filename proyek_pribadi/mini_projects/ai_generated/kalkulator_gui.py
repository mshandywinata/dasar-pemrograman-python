import tkinter as tk

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

root = tk.Tk()
root.title("Calculator")

screen = tk.StringVar()

entry = tk.Entry(root, textvar=screen, font="lucida 20 bold")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['.', '0', '=', '+']
]

for i in range(4):
    for j in range(4):
        button = tk.Button(root, text=buttons[i][j], font='lucida 15 bold')
        button.grid(row=i + 1, column=j)
        button.bind("<Button-1>", calculate)

clear = tk.Button(root, text="C", font='lucida 15 bold')
clear.grid(row=5, column=0)
clear.bind("<Button-1>", calculate)

root.mainloop()
