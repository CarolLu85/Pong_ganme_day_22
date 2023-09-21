from turtle import Turtle
SCORE_COORDINATES = [(60, 240), [-50, 240]]
FONT = ('Arial', 24, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreboard_list = []
        self.create_two_scores()
        # self.right = SCORE_COORDINATES[0]
        # self.left = SCORE_COORDINATES[1]
        self.rightpoint = 0
        self.leftpoint = 0
        self.update()


    def create_two_scores(self):
        for i in SCORE_COORDINATES:
            score = Turtle()
            score.hideturtle()
            score.penup()
            score.color("white")
            score.goto(i)
            self.scoreboard_list.append(score)


    def update(self):
        self.scoreboard_list[1].write(f"{self.leftpoint} ", False, "left", FONT)
        self.scoreboard_list[0].write(f"{self.rightpoint} ", False, "right", FONT)


    def update_leftscore(self):
        self.leftpoint += 1
        self.scoreboard_list[1].clear()
        self.scoreboard_list[1].write(f"{self.leftpoint} ", False, "left", FONT)
        return self.leftpoint


    def update__rightscore(self):
        self.rightpoint += 1
        self.scoreboard_list[0].clear()
        self.scoreboard_list[0].write(f"{self.rightpoint} ", False, "right", FONT)
        return self.rightpoint






