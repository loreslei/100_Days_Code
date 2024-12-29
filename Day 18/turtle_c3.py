from turtle import Turtle, Screen
from random import *
#import turtle as t --> using alias
turtle = Turtle()

turtle.shape("turtle")

turtle.color("cornflowerblue")


my_screen = Screen()
my_screen.colormode(255)

def draw_poligon(sides):
    angle = 360/sides
    #colormode(255)
    c1 = randint(0,255)
    c2 = randint(0,255)
    c3 = randint(0,255)
    turtle.pencolor(c1,c2,c3)
    for _ in range(sides):
        turtle.forward(100)
        turtle.right(angle)
    
    
for i in range(3, 11):
    draw_poligon(i)



my_screen.exitonclick()


