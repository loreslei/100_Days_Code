from turtle import Turtle
START_POINT = (0,0)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(START_POINT)
        self.x_move = 10
        self.y_move = 10
        self.velocity = 0.1
        
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1
        self.velocity /= 1.2
        
    def restart(self):
        self.goto(START_POINT)
        self.velocity = 0.1
        self.bounce_x()