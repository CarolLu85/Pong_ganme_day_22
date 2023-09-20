from turtle import Turtle
# PADDLE_COORDINATES = [(350, 0), (350, 20), (350, 40), (350, 60), (350, 80)]
UP = 90
DOWN = 270

class Paddle():

    def __init__(self):
        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.shapesize(5, 1)
        self.paddle.goto(350, 0)
    #     1 = 20 像素


    def move_up(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + 20)

    def move_down(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - 20)



