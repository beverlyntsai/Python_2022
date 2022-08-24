from  tkinter  import *
tk=Tk()
canvas=Canvas(tk,width=1000, height=500)
canvas.pack()
canvas.create_polygon(20,20,60,100,100,20, fill='green')
