import tkinter as tk

root = tk.Tk()
root.title('Hello')
root.geometry('300x300')
root.config(bg = 'PINK')


box = tk.Label(
    root,
    text = 'Hello\nTkinter!',
    bg = 'BLACK',
    fg = 'YELLOW'
)
box.pack(padx = 90, pady = 90)

root.mainloop()