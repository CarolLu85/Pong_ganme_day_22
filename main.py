import time
from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

paddle = Paddle()

screen.listen()
screen.onkey(paddle.move_up_rightside, "Up")
screen.onkey(paddle.move_down_rightside, "Down")
screen.onkey(paddle.move_up_leftside, "w")
screen.onkey(paddle.move_down_leftside, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)









screen.exitonclick()