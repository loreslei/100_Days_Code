from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("pink")
        self.penup()
        self.reset()
        self.setheading(90)
        
        
    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
            
        
    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y < - FINISH_LINE_Y:
            new_y = - FINISH_LINE_Y
        self.goto(self.xcor(), new_y)

    def completed_level(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False
    
    def reset(self):
        self.goto(STARTING_POSITION)