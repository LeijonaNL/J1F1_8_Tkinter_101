import tkinter
window = tkinter.Tk()
x = 0
y = 0
index = 0

colors_List = ['YELLOW', 'ORANGE', 'RED', 'PURPLE', 'BLACK']

def update(I, x, y):
    if I == len(colors_List):
        window.destroy()
        exit()

    x+=50
    y+=50

    window.title('My first window')
    window.geometry(f'{x}x{y}')
    window.resizable(True, True)

    window.config(bg = colors_List[I])
    window.after(1000, lambda:update(I, x, y))
    I += 1
    
update(index, x, y)

window.mainloop()