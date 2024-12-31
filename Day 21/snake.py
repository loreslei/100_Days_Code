from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SIZE = 20
STARTING_P = 3

class Snake:
    def __init__(self):
        self.body = []
        self.position = []
        self.create_snake()
        self.head = self.body[0]
        
    def create_snake(self):
        for pos in range(STARTING_P):
            self.add_body_part(pos)
            self.position.append(pos)
            
    def extend(self):
        #add a new part of the body to the snake
        new_pos = self.position[-1] + 1
        self.position.append(new_pos)
        self.add_body_part(new_pos)
        
    def add_body_part(self, position):
        new_body = Turtle(shape="square")
        new_body.color("white")
        new_body.penup()
        new_body.goto(position*-SIZE, 0)
        new_body.speed(0)
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
            