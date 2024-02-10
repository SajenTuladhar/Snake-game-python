from tkinter import*
import random

#declaring constants for the game
GAME_WIDTH=700
GAME_HEIGHT=700
SPEED=40
SPACE_SIZE=50
BODY_PARTS=2
SNAKE_COLOR="PINK"
FOOD_COLOR="White"
BG= "BLACK"

class snake:
    def __init__(self) :
        self.body_size=BODY_PARTS
        self.coordinates=[]
        self.squares=[]

        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tag="snek")
            self.squares.append(square)
class food:
    def __init__(self):
        x= random.randint(0,(GAME_WIDTH/SPACE_SIZE )-1)  * SPACE_SIZE
        y= random.randint(0,(GAME_HEIGHT/SPACE_SIZE )-1)  * SPACE_SIZE

        self.coordinates=[x,y]
        canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR,tag="food")
        
def next_turn(Snake,Food):
    x,y= snake.coordinates[0]
    
    if direction =="up":
         y-= SPACE_SIZE
    elif direction=="down":
         y+= SPACE_SIZE
    elif direction=="left":
         x-= SPACE_SIZE
    elif direction=="right":
         x+= SPACE_SIZE

    snake.coordinates.insert(0,(x,y))
    square= canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR) 
    snake.squares.insert(0,square)
    
    del snake.coordinates[-1]
    canvas.delete(snake.squares[-1])
    del snake.squares[-1]
    window.after(SPEED, next_turn, snake,food)

def change_direction(new_direction):
    pass

def check_collision():
    pass

def death():
    pass

window=Tk()
window.title("Snake game")
window.resizable(False,False) # makes window size un-resizeable

score=0
direction= "down"

score_label=Label(window,text="Score:{}".format(score),font=('consolas',50))
score_label.pack()

canvas= Canvas(window,bg=BG,height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.pack()

window.update()
window_width= window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

x=int((screen_width/2)-(window_width/2))
y=int((screen_height/2)-(window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

snake= snake()
food= food()
next_turn(snake,food)
window.mainloop()