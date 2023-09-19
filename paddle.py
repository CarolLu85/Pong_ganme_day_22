from turtle import Turtle
PADDLE_COORDINATES = [(350, 0), (350, 20), (350, 40), (350, 60), (350, 80)]
UP = 90
DOWN = 270

class Paddle():
    def __init__(self):
        self.paddle_list = []
        self.create_paddle()
        self.head = self.paddle_list[0]

    def create_paddle(self):
        for i in PADDLE_COORDINATES:
            new_paddle = Turtle("square")
            new_paddle.color("white")
            new_paddle.penup()
            new_paddle.goto(i)
            self.paddle_list.append(new_paddle)

    def paddle_move(self):
        for i in range(len(self.paddle_list) - 1, 0, -1):
            x = self.paddle_list[i - 1].xcor()
            y = self.paddle_list[i - 1].ycor()
            self.paddle_list[i].goto(x, y)


    def move_up(self):
        self.head.setheading(UP)

    def move_down(self):
        self.head.setheading(DOWN)