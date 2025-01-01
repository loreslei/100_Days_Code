from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

LIMIT = 275
DISTANCE = 50
X_LIMIT_PADDLE = 320
X_LIMIT_SCREEN = 380

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.tracer(0)


paddle_a = Paddle(350, 0)
paddle_b = Paddle(-350, 0)

scoreboard = Scoreboard()

ball = Ball()

screen.listen()

screen.onkey(paddle_a.up, "Up")
screen.onkey(paddle_a.down, "Down")

screen.onkey(paddle_b.up, "w")
screen.onkey(paddle_b.down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.velocity)
    screen.update()
    ball.move()
    
    #Detect collision with wall
    if ball.ycor() > LIMIT or ball.ycor() < -LIMIT:
        #needs to bounce
        ball.bounce_y()
        
    #Detect collision with paddle
    if ball.distance(paddle_a) < DISTANCE and ball.xcor() > X_LIMIT_PADDLE or ball.distance(paddle_b) < DISTANCE and ball.xcor() < -X_LIMIT_PADDLE:
        ball.bounce_x()
        
    #Detect when paddle_a miss
    if ball.xcor() > X_LIMIT_SCREEN:
        ball.restart()
        scoreboard.increase_a()
    
    #Detect when paddle_b miss
    if ball.xcor() < -X_LIMIT_SCREEN:
        ball.restart()
        scoreboard.increase_b()   
        
 
        

screen.exitonclick()