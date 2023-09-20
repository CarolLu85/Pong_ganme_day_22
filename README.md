# Pong_game_day_22
1.def __init__(self):
        super().__init__()
        self.ball = Turtle("square")
        self.ball.shapesize(1, 1)
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, -280)

2.def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,1)
        self.color("white")
        self.penup()
        self.goto(0, -280)
At the beginning, when i started  to create the ball class, i used the 1st version.an error occurred when i tried to compare the distance
between the ball and the paddle in Main.py. i basically typed ball.xcor() and ycor() to get the coordiniates of the ball. but nothing came out.
the reason is because ball.xcor() the ball here is an object of Ball. i was trying to get the attribute "ball" 's xcor and ycor.
it would work ball.ball.xcor. but it doesnt make any sense. 

to tackle this task, the most difficult part for me is the bounce method. at the beginning, i could only make my ball move one step back. i thought
i should put this in a loop. it still didnt work out. then i got back to the lecture, got this *-1 idea, then i worked out this bounce method.
so via using *-1, it just simplely changes the direction, with the move method outside the if statement will keep the ball moving.
