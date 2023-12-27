import turtle
import random
import time

drawing_board=turtle.Screen()
drawing_board.bgcolor("Light blue")
drawing_board.title("Turtle desk")
drawing_board.screensize(500,500,"Light blue")
FONT = ("Verdana",30, "normal")
score =0

liste1=[]




#score Turtle
score_turtle=turtle.Turtle()
score_turtle.color("blue")

#score Turtle
time_turtle=turtle.Turtle()
time_turtle.color("blue")

grid_size =13


def score_height():

    top_height=drawing_board.window_height() /2
    y = top_height * 0.95
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.goto( 0,y)
    score_turtle.write("Score:", move=False, align="center", font=FONT)
def make_turtle(x,y):
    def get_mouse_click_coor(x, y):
        #print(x, y)
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(f"Score {score}", move=False, align="center", font=FONT)


    mouse = turtle.Turtle()
    mouse.onclick(get_mouse_click_coor)
    mouse.color("Green")
    mouse.shape("turtle")
    mouse.shapesize(2)
    mouse.penup()
    mouse.goto(grid_size * x, grid_size * y)
    liste1.append(mouse)

cordinat_x = [-20,-15,-10,-5,0,5,10,15,20]
cordinat_y = [15,10,5,0,-5,-10,-15,-20]

def array_show ():
    for x in cordinat_x:
        for y in cordinat_y:
            make_turtle(x,y)

def hide_turtle():
    for t in liste1:
        t.hideturtle()

def randomly_show():
    hide_turtle()
    random.choice(liste1).showturtle()
    drawing_board.ontimer(randomly_show, 500)

def timer_turtle(time):
    top_height = drawing_board.window_height() / 2
    y = top_height * 0.95
    time_turtle.hideturtle()
    time_turtle.penup()
    time_turtle.goto(9, y - 35)
    time_turtle.clear()
    if time >0 :
        time_turtle.clear()
        time_turtle.write("Time: {}".format(time), move=False, align="center", font=FONT)
        drawing_board.ontimer(lambda: timer_turtle(time-1),1000)
    else:
        time_turtle.clear()
        hide_turtle()
        time_turtle.write("Game Over", move=False, align="center", font=FONT)
        breakpoint()




def start_game():
    turtle.tracer(0)
    score_height()
    array_show()
    hide_turtle()
    randomly_show()
    timer_turtle(20)
    turtle.tracer(1)

start_game()

turtle.mainloop()
