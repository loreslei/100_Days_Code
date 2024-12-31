from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_P = [(0,0), (-20,0), (-40,0)]

class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        
    def create_snake(self):
        for pos in STARTING_P:
            self.add_body_part(pos)
            
    def extend(self):
        #add a new part of the body to the snake
        self.add_body_part(self.body[-1].position())
        
    def add_body_part(self, position):
        new_body = Turtle(shape="square")
        new_body.color("white")
        new_body.penup()
        new_body.goto(position)
        self.body.append(new_body)
            
            
    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y) 
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            