from turtle import Turtle, Screen
#import turtle as t --> using alias
turtle = Turtle()

turtle.shape("turtle")

turtle.color("cornflowerblue")

def square():
    turtle.right(90)
    turtle.forward(100)
    
    
for i in range(4):
    square()

my_screen = Screen()

my_screen.exitonclick()


