import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
ball.draw_dashline()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(paddle.move_up_rightside, "Up")
screen.onkey(paddle.move_down_rightside, "Down")
screen.onkey(paddle.move_up_leftside, "w")
screen.onkey(paddle.move_down_leftside, "s")

left_score = 0
right_score = 0

game_on = True
while game_on:
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_up_down()
    if (abs(paddle.left.xcor() - ball.xcor()) <= 15 and (paddle.left.ycor() - 50 <= ball.ycor() <= paddle.left.ycor() + 50)) or ((abs(paddle.right.xcor() - ball.xcor()) <= 20 and (paddle.right.ycor() - 50 <= ball.ycor() <= paddle.right.ycor() + 50))):
        ball.bounce_left_right()
    if ball.xcor() < -400:
        ball.reset_position()
        right_score = scoreboard.update__rightscore()
        print(right_score)
    if ball.xcor() > 400:
        ball.reset_position()
        left_score = scoreboard.update_leftscore()
        print(left_score)
    if left_score == 10 or right_score == 10:
        break

    ball.ball_move()
    screen.update()
    time.sleep(0.05)



screen.exitonclick()

# if ball.distance(r_paddle) <50 and ball.xcor()>320  or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
#             ball.bounce_left_right()