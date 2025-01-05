from turtle import Turtle
class Text(Turtle):
    def __init__(self, x, y, text):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(text, align="center")
        
        
    def update_score(self, text):
        self.clear()
        self.write(text, align="center")