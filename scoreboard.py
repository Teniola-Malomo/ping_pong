from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(arg=self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    # Dosn't work
    # def screen_divider(self):
    #     self.penup()
    #     self.hideturtle()
    #     self.pencolor("white")
    #     self.pensize(width=5)
    #     self.goto(0, 280)
    #     self.setheading(270)
    #     for i in range(13):
    #         self.penup()
    #         self.forward(20)
    #         self.pendown()
    #         self.forward(20)


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Game Over", align="center", font=("Arial", 30, "normal"))
