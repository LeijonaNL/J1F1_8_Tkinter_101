items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import tkinter as tk
from random import choice

window = tk.Tk()
window.title('Grabbelton')
window.geometry('500x400')

button = tk.Button(
    text = 'Grabbelen',
    bg = 'WHITE',
    fg = 'BLACK'
)
button.pack(
    ipadx = 50,
    ipady = 50
)

label = tk.Label(
    window,
    bg = 'BLACK',
    fg = 'WHITE',
    font = ('Arial', 25)
    )

def labelF(itemV):
    if len(items) <= 0:
        label.config(text = "Sorry,\n je hebt alles al gegrabbeld.")
    else:
        label.config(text = f"Gefeliciteerd,\n je hebt een {itemV} gegrabbeld!")

    label.pack(
    ipadx = 300,
    ipady = 50,
    padx = 50,
    pady = 50
    )

def grabbel(self):
    if len(items) != 0:
        item = choice(items)
        labelF(item)
        items.remove(item)
    else:
        labelF(self)

button.bind('<Button-1>', grabbel)

window.mainloop()