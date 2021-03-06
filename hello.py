import tkinter as tk
import random


def bot():
    label = tk.Label(text='Hello World!')  # ラベルを定義
    x = random.randrange(640)
    y = random.randrange(480)
    label.place(x=x, y=y)
    return


window = tk.Tk()
window.title('Title')
window.geometry('640x640')

btn = tk.Button(window, text='Hello!', command = bot)
btn.place(x=10, y=10)

btn.mainloop()
