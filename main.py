import time
from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)
screen.listen()

paddle = Paddle()
paddle.create_paddle()

screen.onkey(paddle.move_up, "Up")
screen.onkey(paddle.move_down, "Down")

game_on = True
while game_on:
    paddle.paddle_move()
    screen.update()
    time.sleep(0.1)










screen.exitonclick()