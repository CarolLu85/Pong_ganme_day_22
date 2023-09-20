from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        # self.goto(0, 0)


    # Turtle here is the super class, so that now, Ball is the subclass of Turtle.
    # Ball inherited all the properties and methods from Turtle. so now,when you use distance
    # method, there would be an error coming up saying ball has no attritue of distance.
    def draw_dashline(self):
        dash = Turtle()
        dash.color("white")
        dash_length = 10
        gap_length = 5
        num_dashes = 36
        dash.penup()
        dash.goto(0, -260)
        dash.pendown()
        for _ in range(num_dashes):
            dash.hideturtle()
            dash.setheading(90)
            dash.forward(dash_length)
            dash.penup()
            dash.forward(gap_length)
            dash.pendown()

    def ball_move(self):
        self.setx(self.xcor() - self.x_move)
        self.sety(self.ycor() + self.y_move)
        # new_x = self.xcor() + 10
        # new_y = self.ycor() + 10
        # self.goto(new_x, new_y)



    def bounce_up_down(self):
        self.y_move *= -1


    def bounce_left_right(self):
        self.x_move *= -1

    # the main role of these two bounce methods is to changing the ball direction.