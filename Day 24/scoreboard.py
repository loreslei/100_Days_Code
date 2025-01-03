from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.get_high_score()}", align=ALIGNMENT, font=FONT)

    
    def reset(self):
        if self.score > int(self.high_score):
            self.set_high_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
        
    def get_high_score(self):
        with open("Day 24/data.txt") as file:
            higher_score = file.read()
        return higher_score
    
    def set_high_score(self):
        with open("Day 24/data.txt", mode="w") as file:
            file.write(f"{self.score}")