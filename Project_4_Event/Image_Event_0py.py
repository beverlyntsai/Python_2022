import time
from tkinter import*
tk=Tk()
canvas=Canvas(tk,width=400,height=400)
canvas.pack()
my_image=PhotoImage(file='d:\\Beverlyn\\Python\\Projects\\GoodJob.png')
canvas.create_image(15,15,anchor=NW,image=my_image)


def moveImage(event):
    canvas.move(1,5,5)

canvas.bind_all('<KeyPress-Return>',moveImage)


