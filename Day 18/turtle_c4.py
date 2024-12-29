from turtle import Turtle, Screen
from random import *
#import turtle as t --> using alias
turtle = Turtle()

turtle.shape("turtle")

turtle.color("cornflowerblue")


my_screen = Screen()
my_screen.colormode(255)

def rn_walk():
    rn_number = randint(0, 3)
    turtle.speed(10)
    turtle.pensize(10)
    if rn_number == 0:
        turtle.left(90)
        turtle.forward(100)
    elif rn_number == 1:
        turtle.right(90)
        turtle.forward(100)
    elif rn_number == 2:
        turtle.forward(100)
    elif rn_number == 3:
        turtle.backward(100)
    #colormode(255)
    c1 = randint(0,255)
    c2 = randint(0,255)
    c3 = randint(0,255)
    turtle.color(c1,c2,c3)
    
while True:
    rn_walk()


my_screen.exitonclick()


