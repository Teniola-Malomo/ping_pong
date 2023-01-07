from turtle import Screen # ,Turtle
from ping_pong.paddle import Paddle
from ping_pong.ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Screen divider for players
# t = Turtle()
# t.penup()
# t.hideturtle()
# t.pencolor("white")
# t.pensize(width=5)
# t.goto(0, 280)
# t.setheading(270)
# for i in range(13):
#     t.penup()
#     t.forward(20)
#     t.pendown()
#     t.forward(20)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

ball = Ball()
scoreboard = ScoreBoard()

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    # Detect Collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect Collision with Paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect R Paddles Misses
    if ball.xcor() > 300:
        ball.reset_position()
        time.sleep(1.00)
        scoreboard.l_point()

    # Detect L Paddles Misses
    if ball.xcor() < -300:
        ball.reset_position()
        time.sleep(1.00)
        scoreboard.r_point()


screen.exitonclick()
