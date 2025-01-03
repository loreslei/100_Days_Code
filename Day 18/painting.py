import colorgram
from turtle import Turtle, Screen
from random import *
# Extract 6 colors from an image.
rgb_colors = []
colors = colorgram.extract("Day 18\image.jpg", 8)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)


#import turtle as t --> using alias
turtle = Turtle()
my_screen = Screen()
my_screen.colormode(255)
turtle.hideturtle()
turtle.penup()
turtle.setheading(225)
turtle.fd(300)
turtle.setheading(0)
turtle.speed(0)
def millionare():
    rn_color = choice(rgb_colors)
    turtle.dot(20, rn_color)
    turtle.fd(50)
    
number_of_dots = 100   

for dot_count in range(1, number_of_dots + 1): 
    millionare()
    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

my_screen.exitonclick()



