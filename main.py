from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

#in_pos = [(350, 0), (-350, 0)]

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

score = Scoreboard()

game_on = True

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    score.update_scoreboard()

    ball.move()

    #detect collision w wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect if R paddle missed
    if ball.xcor() > 390:
        ball.reset()
        score.l_point()

    #detect if L paddle missed:
    if ball.xcor() < -390:
        ball.reset()
        score.r_point()

    #detect collision w paddle
    if ball.distance(r_paddle) < 40 and ball.xcor() > 320 or ball.distance(l_paddle) < 40 and ball.xcor() < -320:
        ball.bounce_x()



screen.exitonclick()