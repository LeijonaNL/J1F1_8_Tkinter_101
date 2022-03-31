import tkinter as tk
from datetime import datetime
    
root = tk.Tk()
root.geometry('500x300')
root.title('Clock')

time = datetime.now()
now = time.strftime("%d/%m/%Y %H:%M:%S")

label = tk.Label(
        root,
        text = now,
        bg = 'BLACK',
        fg = 'WHITE',
        font = ('Arial', 30)
    )

label.pack(
    ipadx = 400,
    ipady = 400
)

def update():
    time = datetime.now()
    now = time.strftime("%d/%m/%Y %H:%M:%S")
    label.configure(text=now)
    root.after(1000, lambda:update())

update()

root.mainloop()

# Geen gebruik van stringVar is goedgekeurd door Stijn nadat we er beide niet uit kwamen hoe het hier in gebruikt zou worden.