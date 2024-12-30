from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)
    
def move_backwars():
    tim.backward(10)
    
def turn_clockwise():
    tim.left(10)
    
def turn_counter_clockwise():
    tim.right(10)

def reset():
    tim.home()
    tim.clear()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwars)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=reset)

screen.exitonclick()