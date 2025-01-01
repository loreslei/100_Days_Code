from turtle import Turtle
FONT = ("Courier", 80, "normal")
ALIGNMENT = "center"
X_POS = 100
Y_POS = 190

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.a_score = 0
        self.b_score = 0
        self.update_score()
        
        
        
        
        
        
    def update_score(self):
        self.clear()
        self.goto(-X_POS, Y_POS)
        self.write(self.b_score, align=ALIGNMENT, font=FONT)
        
        self.goto(X_POS, Y_POS)
        self.write(self.a_score, align=ALIGNMENT, font=FONT)
        
    def increase_a(self):
        self.a_score += 1
        self.update_score()
        
    def increase_b(self):
        self.b_score += 1
        self.update_score()
        