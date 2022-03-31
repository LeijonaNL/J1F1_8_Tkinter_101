import tkinter
window = tkinter.Tk()
x = 0
y = 0
left = 6


def update(left, x, y):

    x+=50
    y+=50

    window.title('My first window')
    window.geometry(f'{x}x{y}')
    window.resizable(True, True)

    if left == 6:
        pass
    elif left == 5:
        window.config(bg = 'YELLOW')
    elif left == 4:
        window.config(bg = 'ORANGE')
    elif left == 3:
        window.config(bg = 'RED')
    elif left == 2:
        window.config(bg = 'PURPLE')
    elif left == 1:
        window.config(bg = 'BLACK')
    else:
        window.destroy()

    window.after(1000, lambda:update(left, x, y))
    left-=1


update(left, x, y)

window.mainloop()