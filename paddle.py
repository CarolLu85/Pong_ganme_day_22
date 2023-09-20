from turtle import Turtle
PADDLE_COORDINATES = [(380, 0), (-385, 0)]


class Paddle():

    def __init__(self):
        self.PADDLE_LIST = []
        self.create_paddle()
        self.right = self.PADDLE_LIST[0]
        self.left = self.PADDLE_LIST[1]
    #     1 = 20 像素

    def create_paddle(self):
        for i in PADDLE_COORDINATES:
            paddle = Turtle("square")
            paddle.color("white")
            paddle.penup()
            paddle.shapesize(5, 1)
            self.PADDLE_LIST.append(paddle)
            paddle.goto(i)



    def move_up_rightside(self):
        self.PADDLE_LIST[0].goto(self.PADDLE_LIST[0].xcor(), self.PADDLE_LIST[0].ycor() + 50)
    def move_down_rightside(self):
        self.PADDLE_LIST[0].goto(self.PADDLE_LIST[0].xcor(), self.PADDLE_LIST[0].ycor() - 50)


    def move_up_leftside(self):
        self.PADDLE_LIST[1].goto(self.PADDLE_LIST[1].xcor(), self.PADDLE_LIST[1].ycor() + 50)

    def move_down_leftside(self):
        self.PADDLE_LIST[1].goto(self.PADDLE_LIST[1].xcor(), self.PADDLE_LIST[1].ycor() - 50)
