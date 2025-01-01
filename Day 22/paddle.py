from turtle import Turtle

UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.shape("square")
        self.color("white")
        self.left(UP)
        self.goto(x, y)
        
        
        
        
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)