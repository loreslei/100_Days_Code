from turtle import Turtle, Screen
from random import *
#import turtle as t --> using alias
turtle = Turtle()

turtle.shape("turtle")

turtle.color("cornflowerblue")


my_screen = Screen()
my_screen.colormode(255)

def draw_spiro(size_gap):
    #colormode(255)
    turtle.speed(0)
    
    for _ in range(int(360/size_gap)):
        c1 = randint(0,255)
        c2 = randint(0,255)
        c3 = randint(0,255)
        turtle.pencolor(c1,c2,c3)
        turtle.circle(100)
        current_heading = turtle.heading()
        turtle.setheading(current_heading + size_gap)
    
    
draw_spiro(5)



my_screen.exitonclick()


