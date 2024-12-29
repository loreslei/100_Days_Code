from turtle import Turtle, Screen
#import turtle as t --> using alias
turtle = Turtle()

turtle.shape("turtle")

turtle.color("cornflowerblue")

for i in range(15):    
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
        


my_screen = Screen()

my_screen.exitonclick()


