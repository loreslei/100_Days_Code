from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT_L = "left"
ALIGNMENT_C = "center"

TOP_CORNER = (-280, 250)
CENTER = (0,0)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.update_scoreboard()

    
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
    
    
    def update_scoreboard(self):
        self.clear()
        self.goto(TOP_CORNER)
        self.write(f"Level: {self.level}", align=ALIGNMENT_L, font=FONT)
        
        
    def game_over(self):
        self.goto(CENTER)
        self.write("GAME OVER! 😂", align=ALIGNMENT_C, font=FONT)
        