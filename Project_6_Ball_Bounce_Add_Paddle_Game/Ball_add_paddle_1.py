from tkinter import *
import random
import time

class Ball:
    def __init__(self,canvas,paddle,score,color):
        self.canvas=canvas
        self.paddle=paddle
        self.score=score
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        starts=[-2,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.hit_bottom=False
    def hit_paddle(self,pos):
       
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                return True
                
        return False
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)

        if pos[1]<=0:
            self.y=1
        if pos[3]>=self.canvas_height:
            #self.y=-1
            self.hit_bottom=True
        if self.hit_paddle(pos)==True:
            self.score+=1
            self.y=-1
            print("score:"+str(self.score))
        if pos[0]<=0:
            self.x=1
        if pos[2]>=self.canvas_width:
            self.x=-1

    def getScore(self):
        return self.score
class Paddle:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x=0
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos=self.canvas.coords(self.id)
        #print(self.canvas.coords(self.id))
        if pos[0]<=0:
            self.x=0
        elif pos[2]>=self.canvas_width:
            self.x=0
    def turn_left(self,evt):
        self.x=-3
    def turn_right(self,evt):
        self.x=3

tk=Tk()
tk.title("Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
tk.update()
#should let score as varialbe in ball so, it will get update everytime it hit the paddle


paddle=Paddle(canvas,'blue')
ball=Ball(canvas,paddle,0,'red')

while 1:

    if ball.hit_bottom==False:
        ball.draw()
        paddle.draw()
    if ball.hit_bottom==True:
        canvas.create_text(300, 50, text="Game Over: Your score is "+str(ball.score), fill="black", font=('Helvetica 15 bold'))
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    
