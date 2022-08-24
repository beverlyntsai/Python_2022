import time
from tkinter import*
tk=Tk()
canvas=Canvas(tk,width=800,height=800)
canvas.pack()
my_image=PhotoImage(file='d:\\Beverlyn\\Python\\Projects\\GoodJob.png')
canvas.create_image(400,400,anchor=CENTER,image=my_image)


def moveImage(event):
    if event.keysym=='Up':
        canvas.move(1,0,-100)
    elif event.keysym=='Down':
        canvas.move(1,0,100)        
    elif event.keysym=='Left':
        canvas.move(1,-100,0)
    else:
        canvas.move(1,100,0)

canvas.bind_all('<KeyPress-Up>',moveImage)
canvas.bind_all('<KeyPress-Down>',moveImage)
canvas.bind_all('<KeyPress-Left>',moveImage)
canvas.bind_all('<KeyPress-Right>',moveImage)


