from  tkinter  import *
tk=Tk()
canvas=Canvas(tk,width=1000, height=500)
canvas.pack()
canvas.create_rectangle(20,20,300,50,fill='red')
